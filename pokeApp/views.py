from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from pokeApp.forms import *
import requests
import sys

from pokeApp.models import Pokemon


def index(request):
    allPokemons = Pokemon.objects.all()
    template = loader.get_template('pokedex/index.html')
    context = {'allPokemons': allPokemons}
    return HttpResponse(template.render(context, request))


def fetchDataFromOnlineAPI(request):

    #Fetch 20 first pokemons from Online API
    for pokeNum in range(1, 21):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(pokeNum))
        object = response.json()

        newPokemon = Pokemon()
        newPokemon.number = pokeNum

        for prop, value in object.items():
            if prop == "name":
                newPokemon.name = value
            if prop == "types":
                for typeNum, valeur in value[0].items():
                    if typeNum == "type":
                        oui = valeur
                        for typeNameKey, typeNameValue in oui.items():
                            if typeNameKey == "name":
                                newPokemon.pokeType = typeNameValue
            if prop == "sprites":
                allSprites = value
                for frontSpriteKey, frontSpriteValue in allSprites.items():
                    if frontSpriteKey == 'front_default':
                        newPokemon = frontSpriteValue
    return HttpResponse("oui")

def authentification(request):
    if request.method == 'GET':
        form = authentification(request.GET)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                return render(request, 'pokedex/index.html', {})
            else:
                return render(request, 'pokedex/authentification.html', {})
    return render(request, 'pokedex/authentification.html', {})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('')
    else:
        form = UserCreationForm()
    return render(request, 'pokedex/signUp.html', {'form': form})

def addPokemon(request):
    if request.method == 'POST':
        form = addPokemonForm(request.POST)
        if form.is_valid():
            form.save()
            _name = form.cleaned_data.get('name')
            _number = form.cleaned_data.get('number')
            _pokeType = form.cleaned_data.get('pokeType')
            _imageLink = form.cleaned_data.get('imageLink')
            newPoke = Pokemon(_name, _number, _pokeType, _imageLink)
            newPoke.save()
            return redirect('')
    else:
        form = addPokemon()
    return render(request, 'pokedex/addPokemon.html', {'form': form})