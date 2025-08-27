import importlib
import unittest

# Importa o submódulo de forma explícita e robusta
calculadora = importlib.import_module("unitest.pacote.calculadora")


class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(calculadora.soma(2, 3), 5)
