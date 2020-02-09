from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authentification/', views.authentification, name='authentification'),
    path('signup/', views.signup, name='authentification'),
    path('addPokemon/', views.addPokemon, name='addPokemon'),
    path('fetchDataOnline/', views.fetchDataFromOnlineAPI, name='fetchDataFromOnlineAPI'),
]