import pytest


def print_hi(name):
    print(f'Hi, {name}')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividiras por zero'


if __name__ == '__main__':
    print_hi('Vivis')

    resultado = somar(8, 7)
    print(f'A soma é: {resultado}')


