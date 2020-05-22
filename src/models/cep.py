import requests

from src.decorators import try_request
from typing import Union


class Cep(object):
    URL = 'https://viacep.com.br/ws/'

    @try_request
    def get_cep(self, cep: str) -> dict:
        url = self.URL + cep + '/json'

        response = requests.get(url)

        return response.json()

    @try_request
    def get_cep_by_name(self, uf: str, city: str, street: str) -> Union[list, dict]:
        url = self.URL + f'{uf}/{city}/{street}/json'

        response = requests.get(url)

        return list(response.json())
