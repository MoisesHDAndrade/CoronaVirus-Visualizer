from django.urls import path
from . import views

app_name = 'covid'
urlpatterns = [

    
    path('', views.alphabetic_order, name='alphabetic'),
    path('deaths/', views.ordered_deaths, name='deaths'),
    path('cases/', views.ordered_confirmed, name='cases'),
    path('recovered/', views.ordered_recovered, name='recovered'),
    path('search/', views.search_corona, name='search')
]
