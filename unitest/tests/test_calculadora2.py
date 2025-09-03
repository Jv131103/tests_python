import unittest

# usando o __init__.py do pacote
from unitest.pacote.calculadora import soma, subtracao


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 10), 0)
