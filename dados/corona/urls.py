from django.urls import path
from . import views

app_name = 'covid'
urlpatterns = [

    path('', views.visualiza, name='index'),
    path('search/', views.search_corona, name='search')
]
