from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
from googlesearch import search
from itertools import groupby

def visualiza(request):
    url = 'https://pomber.github.io/covid19/timeseries.json'
    req = requests.get(url)
    retorno = req.json()
    total_confirmed = []
    total_deaths = []
    total_recovered = []
    last_index = []
    atual = {}
    contador = 0
    for item in retorno.values():
        last_index.append(item[-1])
        total_confirmed.append(item[-1]['confirmed'])
        total_deaths.append(item[-1]['deaths'])
        total_recovered.append(item[-1]['recovered'])
    
    for key in retorno.keys():
        atual[key] = last_index[contador]
        contador +=1
    total = {'confirmed': sum(total_confirmed),
             'deaths': sum(total_deaths), 'recovered': sum(total_recovered), }
    return render(request, 'covid.html', {'obj': atual, 'total': total,} )


def search_corona(request):
    url = 'https://pomber.github.io/covid19/timeseries.json'
    req = requests.get(url)
    termo = request.GET.get('termo')
    retorno = req.json()
    key = retorno.keys()
    noticia = []
    if not termo in key:
        messages.add_message(request, messages.ERROR,
                             'Sua busca nao coincide com nosso banco de dados')
        return redirect('covid:index')
    if termo in key:
        dicionario = retorno[termo]
        info = dicionario[-1]
        try:
            [noticia.append(resultados) for resultados in search(f'"{termo} corona virus" nws', stop=3)]
            # for resultados in search(f'"{termo} corona virus" nws', stop=3):
            #     noticia.append(resultados)
        except Exception as e:
            print('Error'+str(e))

    print(noticia)
    return render(request, 'search.html', {'obj': termo, 'info': info, 'noticias': noticia})
