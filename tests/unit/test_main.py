import pytest

from main import somar, subtrair, multiplicar, dividir


def teste_somar():
    # 1- Configurar
    numero_a = 8
    numero_b = 7
    resultado_esperado = 15

    # 2- Executar
    resultado_obtido = somar(numero_a, numero_b)

    # 3- Validar
    assert resultado_obtido == resultado_esperado


lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)
]

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def teste_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1- Configurar
    # utilizada a lista como massa de teste

    # 2- Executar
    resultado_obtido = somar(numero_a, numero_b)

    # 3- Validar
    assert resultado_obtido == resultado_esperado


def teste_dividir_positivo():
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


def teste_dividir_negativo():
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
