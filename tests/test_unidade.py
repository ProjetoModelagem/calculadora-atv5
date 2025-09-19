import unittest
from src.calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    # 3.1 Entrada e Saída
    def test_entrada_saida_soma(self):
        calc = Calculadora()
        r = calc.somar(5, 3)
        self.assertEqual(r, 8)
        self.assertEqual(calc.obter_ultimo_resultado(), 8)

    def test_entrada_saida_subtracao(self):
        calc = Calculadora()
        r = calc.subtrair(5, 3)
        self.assertEqual(r, 2)

    def test_entrada_saida_multiplicacao(self):
        calc = Calculadora()
        r = calc.multiplicar(5, 3)
        self.assertEqual(r, 15)

    def test_entrada_saida_divisao(self):
        calc = Calculadora()
        r = calc.dividir(6, 3)
        self.assertEqual(r, 2)

    # 3.2 Tipagem
    def test_tipagem_invalida(self):
        calc = Calculadora()
        with self.assertRaises(TypeError):
            calc.somar("5", 3)
        with self.assertRaises(TypeError):
            calc.dividir(10, None)

    def test_tipagem_invalida_todas(self):
        calc = Calculadora()
        for func in [calc.subtrair, calc.multiplicar, calc.potencia]:
            with self.assertRaises(TypeError):
                func("a", 1)

    # 3.3 Consistência
    def test_consistencia_historico(self):
        calc = Calculadora()
        calc.somar(2, 3)
        calc.multiplicar(4, 5)
        self.assertEqual(len(calc.historico), 2)
        self.assertIn("2 + 3 = 5", calc.historico)
        self.assertIn("4 * 5 = 20", calc.historico)

    # 3.4 Inicialização
    def test_inicializacao(self):
        calc = Calculadora()
        self.assertEqual(calc.resultado, 0)
        self.assertEqual(len(calc.historico), 0)

    # 3.5 Modificação de Dados
    def test_modificacao_historico(self):
        calc = Calculadora()
        calc.somar(1, 1)
        self.assertEqual(len(calc.historico), 1)
        calc.limpar_historico()
        self.assertEqual(len(calc.historico), 0)

    # 3.6 Limite Inferior
    def test_limite_inferior(self):
        calc = Calculadora()
        r = calc.somar(0, 5)
        self.assertEqual(r, 5)
        r = calc.multiplicar(-1e-10, 2)
        self.assertEqual(r, -2e-10)

    # 3.7 Limite Superior
    def test_limite_superior(self):
        calc = Calculadora()
        r = calc.somar(1e308, 1e308)
        self.assertTrue(r == float('inf') or r > 1e308)

    # 3.8 Valores Fora do Intervalo
    def test_divisao_por_zero(self):
        calc = Calculadora()
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # 3.9 Fluxos de Controle
    def test_fluxos_divisao(self):
        calc = Calculadora()
        r = calc.dividir(10, 2)
        self.assertEqual(r, 5)
        with self.assertRaises(ValueError):
            calc.dividir(10, 0)

    # 3.10 Mensagens de Erro
    def test_mensagens_erro(self):
        calc = Calculadora()
        with self.assertRaises(ValueError) as cm:
            calc.dividir(5, 0)
        self.assertEqual(str(cm.exception), "Divisao por zero nao permitida")

if __name__ == '__main__':
    unittest.main()
