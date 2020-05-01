import json
from urllib.parse import urljoin

import requests

from src.decorators import try_request


class Cep(object):
    URL = 'https://viacep.com.br/ws/'

    @try_request
    def get_cep(self, cep: str) -> json:
        url = self.URL + cep + '/json'

        response = requests.get(url)

        return response

    @try_request
    def get_cep_by_name(self, uf: str, city: str, street: str) -> json:
        url = self.URL + f'{uf}/{city}/{street}/json'

        response = requests.get(url)

        return response
