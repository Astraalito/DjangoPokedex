from django.http import HttpResponse
from django.template import loader
import requests
import sys

from pokeApp.models import Pokemon


def index(request):
    template = loader.get_template('pokedex/index.html')
    context = {}
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
    return HttpResponse("oui")
