# bibliotecas
import json

import pytest
import requests

#from tests.utils.file_manager import ler_csv

# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

# definições das funcões (defs)

def teste_incluir_pet():
    # Configura / Prepara
    # Dados de entrada provem do pet1.json

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 3475757
    pet_nome_esperado = "Luke"
    pet_nome_categoria_esperado = "Cachorro"
    pet_nome_tag_esperado = "Vacinado"

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\A426692\\PycharmProjects\\134Inicial\\vendors\\json\\pet1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def teste_consultar_pet():
    # Configura
    # Dados de Entrada
    pet_id = '3475757'

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 3475757
    pet_nome_esperado = "Luke"
    pet_nome_categoria_esperado = "Cachorro"
    pet_nome_tag_esperado = "Vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))


    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def teste_consultar_pet():
    # Configura
    # Entrada
    pet_id = '3475757'

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 3475757
    pet_nome_esperado = "Luke"
    pet_nome_categoria_esperado = "Cachorro"
    pet_nome_tag_esperado = "Vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))


    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def teste_alterar_pet():
    # Configura
    # Dados de Entrada virão do pet2.json

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 3475757
    pet_nome_esperado = "Luke"
    pet_nome_categoria_esperado = "Cachorro"
    pet_nome_tag_esperado = "Vacinado"
    pet_status_esperado = 'pending'

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\A426692\\PycharmProjects\\134Inicial\\vendors\\json\\pet2.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado

