# Configura
# Bibliotecas/Imports
from selenium import webdriver


# Dados de Entrada
from selenium.webdriver.common.by import By

origem = 'São Paolo'
destino = 'Dublin'
primeiro_nome = 'Viviane'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
titulo_passagens_esperado = 'Flights from São Paolo to Dublin:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'

# Executa
url = 'https://blazedemo.com/'
class Testes:
    # Início
    def setup_method(self):
        # instanciar a biblioteca/motor/engine
        # informar onde está o WebDriver
        self.driver = webdriver.Edge()


    # Fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e/end to end/ ponta a ponta
        # Página Inicial (Home)
        # Executa/Valida
        self.driver.get(url)
        lista = self.driver.find_element(By.NAME('fromPort'))
        lista.click()
        lista.find_element(By.XPATH('//option[ .="São Paolo"]')).click()
        lista = self.driver.find_element(By.NAME('toPort'))
        lista.click()
        lista.find_element(By.XPATH('//option[ .="Dublin"]')).click()
        self.driver.find_element(By.CSS_SELECTOR('input.btn.btn-primary'))



        # Página Lista de Passagens
        # Executa/Valida

        # Página de Compra
        # Executa/Valida

        # Página de Obrigado
        # Executa
        # Valida
