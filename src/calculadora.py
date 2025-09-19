import math

class Calculadora:
    def __init__(self):
        self.historico = []
        self.resultado = 0

    def _verifica_tipo(self, *args):
        for a in args:
            if not isinstance(a, (int, float)):
                raise TypeError("Argumentos devem ser numeros")

    def somar(self, a, b):
        self._verifica_tipo(a, b)
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def subtrair(self, a, b):
        self._verifica_tipo(a, b)
        resultado = a - b
        self.historico.append(f"{a} - {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def multiplicar(self, a, b):
        self._verifica_tipo(a, b)
        resultado = a * b
        self.historico.append(f"{a} * {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def dividir(self, a, b):
        self._verifica_tipo(a, b)
        if b == 0:
            raise ValueError("Divisao por zero nao permitida")
        resultado = a / b
        self.historico.append(f"{a} / {b} = {resultado}")
        self.resultado = resultado
        return resultado

    def potencia(self, base, expoente):
        self._verifica_tipo(base, expoente)
        resultado = base ** expoente
        self.historico.append(f"{base} ^ {expoente} = {resultado}")
        self.resultado = resultado
        return resultado

    def limpar_historico(self):
        self.historico.clear()

    def obter_ultimo_resultado(self):
        return self.resultado
