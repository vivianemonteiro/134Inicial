# Configura
# Bibliotecas/Imports
import pytest
from selenium import webdriver

# Dados de Entrada
from selenium.webdriver.common.by import By

#origem = 'São Paolo'
#destino = 'Dublin'
primeiro_nome = 'Viviane'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
#titulo_passagens_esperado = 'Flights from São Paolo to Dublin:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'

# Executa
url = 'https://blazedemo.com/'


class Testes:
    # Início
   # def setup_method(self):
        # instanciar a biblioteca/motor/engine
        # informar onde está o WebDriver


    # Fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

# Lista para uso como massa de teste
    lista_de_valores = [
        ('São Paolo', 'New York', 'firefox'),
        ('Boston', 'Berlin', 'edge'),
        ('San Diego', 'London', 'firefox'),
        ('Philadelphia', 'Cairo', 'edge')
    ]

    @pytest.mark.parametrize('origem,destino, browser', lista_de_valores)

    # Meio
    def testar_comprar_passagem(self, origem, destino, browser):
        # e2e/end to end/ ponta a ponta
        # Trouxe o setu_method / Iniciação para cá
        match browser:
            case 'edge':
                self.driver = webdriver.Edge()
            case 'firefox':
                self.driver = webdriver.Firefox()

        # Página Inicial (Home)
        # Executa/Valida
        self.driver.get(url)
        lista = self.driver.find_element(By.NAME, 'fromPort')
        lista.click()
        lista.find_element(By.XPATH, f'//option[ .= "{origem}"]').click()
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()
        lista.find_element(By.XPATH, f'//option[ .= "{destino}"]').click()
        lista.click()
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Página Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == f'Flights from {origem} to {destino}:'

        self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) .btn').click()

        # Página de Compra
        # Executa/Valida
        # Preenche nome do comprador
        self.driver.find_element(By.ID, 'inputName').send_keys(primeiro_nome)
        # Seleciona a bandeira do cartão
        lista = self.driver.find_element(By.ID, 'cardType')
        lista.click()
        lista.find_element(By.XPATH, f'//option[ .= "{bandeira}"]').click()
        # Marca o checkbox para ser lembrado
        self.driver.find_element(By.ID, 'rememberMe').click()
        # Aperta o botão de Purchase Flight
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Página de Obrigado
        # Valida
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == mensagem_agradecimento_esperada
        assert self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(2)').text == \
               preco_passagem_esperado
