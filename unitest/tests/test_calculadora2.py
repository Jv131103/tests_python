import unittest

from unitest.pacote.calculadora import soma  # usando o __init__.py do pacote


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
