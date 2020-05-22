from unittest import TestCase
from unittest.mock import patch, mock_open

from src.models.logger import Logger


class TestLogger(TestCase):
    def setUp(self):
        self.logger = Logger()

    @patch('src.models.logger.os')
    def test_se_clear_funciona(self, mock_os):
        self.logger.clear()

        mock_os.remove.assert_called_with(self.logger.FILEPATH)

    @patch('builtins.open', new_callable=mock_open())
    @patch('src.models.logger.os')
    def test_se_create_funciona(self, mock_os, mock_open):
        mock_os.path.exists.return_value = False
        self.logger.create()
        
        mock_os.mkdir.assert_called_with(self.logger.PATH)
        mock_open.assert_called_with(self.logger.FILEPATH, 'w')
