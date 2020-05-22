from unittest import TestCase

from click.testing import CliRunner

from src import cli


class TestCli(TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_cep(self):
        result = self.runner.invoke(cli.cep, '07713045')

        self.assertEqual(result.exit_code, 0)

    def test_get_by_name(self):
        result = self.runner.invoke(cli.name, ['sp', 'osasco', 'sabirigui'])

        self.assertEqual(result.exit_code, 0)
