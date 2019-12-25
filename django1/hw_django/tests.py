import json

from http import HTTPStatus

from django.test import TestCase
from django.test import Client

from django.urls import reverse

from .utils import (
    get_pokemons_list,
    get_pokemon
)


class StatusViewTests(TestCase):
    client = Client()

    def test_health_check_view(self):
        response = self.client.get(reverse('status'))
        assert response.status_code == HTTPStatus.OK

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == HTTPStatus.OK

    def test_pokemons_view(self):
        response = self.client.get(reverse('pokemons'))
        assert response.status_code == HTTPStatus.OK

    def test_pokemon_view(self):
        names = ['bulbasaur', 'squirtle']
        for name in names:
            response = self.client.get(reverse('pokemon', args=[name]))
            assert response.status_code == HTTPStatus.OK


class CheckApiResponseTests(TestCase):
    def setUp(self) -> None:
        self.names = ['bulbasaur', 'squirtle']

    def test_pokemons_list_response(self):
        assert get_pokemons_list().status_code == HTTPStatus.OK

    def test_pokemon_response(self):
        for name in self.names:
            assert get_pokemon(name).status_code == HTTPStatus.OK

    def test_pokemons_list_response_validity(self):
        data = get_pokemons_list().json()
        try:
            json.dumps(data)
        except TypeError:
            self.fail("json is not valid")

    def test_pokemon_response_validity(self):
        for name in self.names:
            data = get_pokemon(name).json()
            try:
                json.dumps(data)
            except TypeError:
                self.fail("json is not valid")
