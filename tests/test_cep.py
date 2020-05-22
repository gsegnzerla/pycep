from unittest import TestCase

from vcr import VCR
import json
from typing import Union
from src.models.cep import Cep


vcr_ = VCR(
    cassette_library_dir='tests/cassetts',
    path_transformer=VCR.ensure_suffix('.yaml'),
    record_mode='once'
)


class TestCep(TestCase):
    def setUp(self):
        self.cep = Cep()

    @vcr_.use_cassette
    def test_get_cep_responde_com_json(self):
        response = self.cep.get_cep('07713045')

        self.assertIsInstance(response, dict)

    @vcr_.use_cassette
    def test_get_cep_by_name_responde_com_json(self):
        response = self.cep.get_cep_by_name('SP', 'São Paulo', 'Eulo Maroni')

        self.assertIsInstance(response, list)

    