from src.logger import Logger
from unittest import TestCase, mock


class TestLogger(TestCase):

    data = {
        "cep": "07713-045",
        "logradouro": "Avenida João Pacheco",
        "complemento": "(Vl S João)",
        "bairro": "Serpa",
        "localidade": "Caieiras",
        "uf": "SP",
        "unidade": "",
        "ibge": "3509007",
        "gia": "2392"
    }

    def setUp(self):
        self.logger = Logger()

    @mock.patch('src.logger.os')
    @mock.patch('builtins.open', new_callable=mock.mock_open())
    def test_se_clear_funciona(self, mock_file, mock_os):
        self.logger.clear()

        mock_os.remove.assert_called_with(self.logger.FILEPATH)
        

    @mock.patch('src.logger.os')
    @mock.patch('builtins.open', new_callable=mock.mock_open())
    def test_se_create_funciona(self, mock_open, mock_os):
        mock_os.path.exists.return_value = False

        self.logger.create()
        
        mock_os.mkdir.assert_called_with(self.logger.PATH)
        mock_os.path.exists.return_value = True

        mock_open.assert_called_with(self.logger.FILEPATH, 'w')

    @mock.patch('src.logger.json.dump')
    @mock.patch('builtins.open', new_callable=mock.mock_open())
    def test_se_store_funciona(self, mock_file, mock_dump):
        self.logger.store(self.data)

        # simple assertion that your open was called
        mock_file.assert_called_with(self.logger.FILEPATH, 'a')

        # assert that you called mock_json with your data
        mock_dump.assert_called_with(
            self.data, mock_file.return_value.__enter__.return_value, indent=4)
