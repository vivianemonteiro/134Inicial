from main import somar, dividir


class TesteContas:
    def teste_somar(self):
        # 1- Configurar
        numero_a = 8
        numero_b = 7
        resultado_esperado = 15

        # 2- Executar
        resultado_obtido = somar(numero_a, numero_b)

        # 3- Validar
        assert resultado_obtido == resultado_esperado

    def teste_dividir_positivo(self):
        # 1- Configurar
        # 1.1 Dados de Entrada
        numero_a = 27
        numero_b = 3

        # 1.2 Resultados Esperados
        resultado_esperado = 9

        # 2- Executar
        resultado_obtido = dividir(numero_a, numero_b)

        # 3- Validar
        assert resultado_obtido == resultado_esperado

    def teste_dividir_negativo(self):
        # 1- Configurar
        # 1.1 Dados de Entrada
        numero_a = 27
        numero_b = 0

        # 1.2 Resultados Esperados
        resultado_esperado = 'Não dividiras por zero'

        # 2- Executar
        resultado_obtido = dividir(numero_a, numero_b)

        # 3- Validar
        assert resultado_obtido == resultado_esperado
