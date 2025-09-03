"""
TDD - Test Driven Development (Desenvolvimento Dirigido a Teste)

RED
1 - Criar um teste e falhar

GREEN
2 - Criar o código e ver se o teste passa

REFACTOR
3 - Melhorar o código
"""

import unittest

from unitest.pacote.baconcomovos import ismultiple_3_or_5


class TestBaconComOvos(unittest.TestCase):
    def test_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            ismultiple_3_or_5('')

    def test_ismultiple_3_or_5_deve_retornar_baconcomovos_se_for_multiplo_de_3_e_5(self):
        entradas = ((n, "baconcomovos") for n in range(15, 151, 15))

        for entrada in entradas:
            with self.subTest(entrada=entrada):
                numero_teste, saida_esperada = entrada
                self.assertEqual(
                    ismultiple_3_or_5(numero_teste),
                    saida_esperada,
                    msg=f"{numero_teste} não retornou {saida_esperada} "
                )

    def test_ismultiple_3_or_5_deve_retornar_passafome_senao_for_multiplo_de_3_e_5(self):
        entradas = (8, 13, 14, 29, 43)
        saida = "passafome"

        for entrada in entradas:
            with self.subTest(entrada=entrada):
                self.assertEqual(
                    ismultiple_3_or_5(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida} "
                )

    def test_ismultiple_3_or_5_deve_retornar_bacon_se_for_multiplo_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21, 24)
        saida = "bacon"

        for entrada in entradas:
            with self.subTest(entrada=entrada):
                self.assertEqual(
                    ismultiple_3_or_5(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida} "
                )

    def test_ismultiple_3_or_5_deve_retornar_ovos_se_for_multiplo_de_5(self):
        entradas = (5, 10, 25, 25, 35, 40, 50)
        saida = "ovos"

        for entrada in entradas:
            with self.subTest(entrada=entrada):
                self.assertEqual(
                    ismultiple_3_or_5(entrada),
                    saida,
                    msg=f"{entrada} não retornou {saida} "
                )
