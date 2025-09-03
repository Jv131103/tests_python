import unittest
from unittest.mock import patch

from unitest.pacote.pessoa import Pessoa


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa("Joao", "Justino")
        self.p2 = Pessoa("Maria", "Júlia")

    def test_pessoa_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.nome, "Joao")
        self.assertEqual(self.p2.nome, "Maria")

    def test_pessoa_attr_nome_e_do_tipo_str(self):
        self.assertIsInstance(self.p1.nome, str)
        self.assertIsInstance(self.p2.nome, str)

    def test_pessoa_attr_sobrenome_tem_o_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, "Justino")
        self.assertEqual(self.p2.sobrenome, "Júlia")

    def test_pessoa_attr_sobrenome_e_do_tipo_str(self):
        self.assertIsInstance(self.p1.sobrenome, str)
        self.assertIsInstance(self.p2.sobrenome, str)

    def test_pessoa_attr_dados_obtidos_inicia_false(self):
        self.assertFalse(self.p1.dados_obtidos)
        self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch("requests.get") as fake_requests:
            fake_requests.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_sucesso_FALHA(self):
        with patch("requests.get") as fake_requests:
            fake_requests.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), "NAO CONECTADO")
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), "NAO CONECTADO")
            self.assertFalse(self.p2.dados_obtidos)

    def test_obter_todos_os_dados_OK_e_FALHA_sequencial(self):
        with patch("requests.get") as fake_requests:
            fake_requests.return_value.ok = True

            self.assertEqual(self.p1.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), "CONECTADO")
            self.assertTrue(self.p2.dados_obtidos)

            fake_requests.return_value.ok = False

            self.assertEqual(self.p1.obter_todos_os_dados(), "NAO CONECTADO")
            self.assertFalse(self.p1.dados_obtidos)

            self.assertEqual(self.p2.obter_todos_os_dados(), "NAO CONECTADO")
            self.assertFalse(self.p2.dados_obtidos)
