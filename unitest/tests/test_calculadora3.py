import unittest

from ..pacote.calculadora import soma


class TestSoma(unittest.TestCase):
    def test_soma_basica(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_varias_entradas(self):
        x_y_saidas = [
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200),
        ]
        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)

    def test_soma_negativos(self):
        self.assertEqual(soma(-1, -2), -3)

    def test_x_ou_y_nao_e_int_ou_float_deve_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('1', 2)
