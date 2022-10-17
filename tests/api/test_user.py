# Done: 1. Criar um teste que adicione um usuário
# Done: 2. Realizar o login e extrair o token da resposta

import json

import requests

url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}


def teste_incluir_usuario():
    # Configura
    # Dados de Entrada
    # Virão do arquivo user1.json

    # Resultados Esperados
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '5757347'

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\A426692\\PycharmProjects\\134Inicial\\vendors\\json\\user1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert resultado_obtido['code'] == codigo_esperado
    assert resultado_obtido[type] == tipo_esperado
    assert resultado_obtido['message'] == mensagem_esperada


def teste_login():
    # Configura
    username = 'juca'
    password = 'bala'

    # Resultado Esperado
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'logged in user session:'

    # Executa
    resultado_obtido = requests.get(
        url=f'{url}/login?username={username}&password={password}',
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert resultado_obtido['code'] == codigo_esperado
    assert resultado_obtido[type] == tipo_esperado
    assert mensagem_esperada.find(corpo_do_resultado_obtido['message'])

    # Extrair

    mensagem_extraida = corpo_do_resultado_obtido.get('message')
    print(f'A mensagem é = {mensagem_extraida}')
    token = mensagem_extraida[23:]
    print(f'O token é = {token}')
