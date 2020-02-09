from django.contrib import admin
from .models import Pokemon


class PokedexAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "pokeType", "imageLink", "user")


admin.site.register(Pokemon, PokedexAdmin)
