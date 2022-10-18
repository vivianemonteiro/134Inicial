# Done: 3. Criar a venda de um pet para um usuário
# Done: 4. Consultar os dados do pet que foi vendido
import os.path

import requests
url = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}

def teste_vender_pet():
    # Configura
    # Dados de entrada
    # Virão do arquivo pedido1.json

    # Resultados esperados
    status_code_esperado = 200
    pedido_id_esperado = 25345757
    pet_id_esperado = 3475757
    status_pedido_esperado = 'placed'

    # Executa
    caminho = os.path.abspath(__file__ + "/../../../") + os.sep + 'vendors' + os.sep + 'json' + os.sep
    resultado_obtido = requests.post(
        url=url + 'store/order',
        headers=headers,
        data=open(caminho + 'pedido1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert resultado_obtido['petId'] == pet_id_esperado
    assert corpo_do_resultado_obtido['status'] == status_pedido_esperado

    # Extrair
    pet_id_extraido = corpo_do_resultado_obtido.get('petId')

    # Realizar a 2ª Transação

    # Configura
    # Dados de Entrada
    # Extraídos da 1ª transação acima

    # Reaultado Esperado
    pet_name_esperado = 'Luke'
    status_code_esperado = 200

    # Executa
    resultado_obtido = requests.get(
        url=url + 'pet/' + str(pet_id_extraido),
        headers=headers
    )

    # Validação
    assert resultado_obtido.status_code == status_code_esperado
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))
    assert corpo_do_resultado_obtido['name'] == pet_name_esperado