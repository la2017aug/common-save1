import requests
from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_pokemons_list, get_pokemon


def status(request):
    return HttpResponse("OK")

def index(request):
    return render(request, 'home.html')


def pokemons(request):
    response = get_pokemons_list()
    results = response.json()['results']
    info = [
        {
            'type': item['name'],
            'pokemons': [p['pokemon']['name'] for p in requests.get(item['url']).json()['pokemon']]
        }
        for item in results
    ]
    return render(request, 'pokemons.html', {'info': info})


def pokemon(request, name):
    response = get_pokemon(name)
    info = response.json()
    return render(request, 'pokemon.html', {'info': info})

