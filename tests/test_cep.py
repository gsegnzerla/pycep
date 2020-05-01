from unittest import TestCase

from vcr import VCR

from src.cep import Cep

vcr_ = VCR(
    cassette_library_dir='tests/cassetts',
    path_transformer=VCR.ensure_suffix('.yaml'),
    record_mode='once'
)


class TestCep(TestCase):

    def setUp(self):
        self.cep = Cep()

    @vcr_.use_cassette
    def test_get_cep(self):
        response = self.cep.get_cep('07713045')

        self.assertEqual(200, response.status_code)

    @vcr_.use_cassette
    def test_get_cep_by_name(self):
        response = self.cep.get_cep_by_name('SP', 'São Paulo', 'Eulo Maroni')

        self.assertEqual(200, response.status_code)
