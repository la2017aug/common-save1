import requests

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


def get_pokemons_list():
    return requests.get(f'{POCKEMON_URL}/type')


def get_pokemon(name):
    return requests.get(f'{POCKEMON_URL}/pokemon/{name}')
