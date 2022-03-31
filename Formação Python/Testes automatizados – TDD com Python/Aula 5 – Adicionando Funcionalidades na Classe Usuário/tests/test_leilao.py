from unittest import TestCase
from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    def setUp(self):
        self.gui = Usuario('Gui', 500.0)
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao('Celular')


    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.propoem(lance_do_yuri)
        self.leilao.propoem(self.lance_do_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_nao_deve_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(ValueError):
            yuri = Usuario('Yuri', 500.0)
            lance_do_yuri = Lance(yuri, 100.0)

            self.leilao.propoem(self.lance_do_gui)
            self.leilao.propoem(lance_do_yuri)


    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_menor_lance_quando_o_leilao_tiver_um_lance(self):
        self.leilao.propoem(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        yuri = Usuario('Yuri', 500.0)
        bru = Usuario('Bru', 500.0)

        lance_do_yuri = Lance(yuri, 100.0)
        lance_do_bru = Lance(bru, 200.0)

        self.leilao.propoem(lance_do_yuri)
        self.leilao.propoem(self.lance_do_gui)
        self.leilao.propoem(lance_do_bru)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    def test_deve_permitir_propor_lance_caso_o_leilao_não_tenha_lances(self):
        self.leilao.propoem(self.lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebido)


    def test_deve_permitir_propro_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.0)

        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoem(self.lance_do_gui)
        self.leilao.propoem(lance_do_yuri)

        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)


    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoem(self.lance_do_gui)
            self.leilao.propoem(lance_do_gui200)

