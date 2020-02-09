from django import forms

from pokeApp.models import User

class addPokemonForm(forms.Form):
    name = forms.CharField(max_length=20)
    number = forms.CharField(max_length=20)
    pokeType = forms.CharField(max_length=20)
    imageLink = forms.CharField(max_length=250)