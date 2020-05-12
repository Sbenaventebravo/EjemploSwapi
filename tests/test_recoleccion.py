import unittest
import json
from unittest.mock import patch
from src.manupulacion import cantidad_de_personajes

class ManipulacionTestCase(unittest.TestCase):

    def test_cantidad_de_personajes_success(self):
        input = {"count": 82}
        output = 82
        cantidad = cantidad_de_personajes(input)
        self.assertEqual(cantidad, output)

    @patch("src.manupulacion.logging.error")
    def test_cantidad_de_personajes_fail(self, mock_error):
        input = {"counter": 82}
        output = -1
        cantidad = cantidad_de_personajes(input)
        self.assertEqual(cantidad, output)
        mock_error.assert_called_once_with("a")
    pass