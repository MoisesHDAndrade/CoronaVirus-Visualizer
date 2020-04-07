from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
from googlesearch import search


def visualiza(request):
    url = 'https://pomber.github.io/covid19/timeseries.json'
    req = requests.get(url)
    retorno = req.json()
    total_confirmed = []
    total_deaths = []
    total_recovered = []
    for item in retorno.values():
        total_confirmed.append(item[-1]['confirmed'])
        total_deaths.append(item[-1]['deaths'])
        total_recovered.append(item[-1]['recovered'])
    total = {'confirmed': sum(total_confirmed),
             'deaths': sum(total_deaths), 'recovered': sum(total_recovered)}
    return render(request, 'covid.html', {'obj': retorno, 'total': total})


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
            for resultados in search(f'"{termo} corona virus" nws', stop=3):
                noticia.append(resultados)
        except Exception as e:
            print('Error'+str(e))

    print(noticia)
    return render(request, 'search.html', {'obj': termo, 'info': info, 'noticias': noticia})
