import unittest

from ..pacote.calculadora import soma


class TestSoma(unittest.TestCase):
    def test_soma_basica(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -2), -3)
