import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBlazeDemoCompra:
    def setup_method(self):
        self.driver = webdriver.Chrome('C:\\Users\\A426692\\PycharmProjects\\134Inicial\\vendors\\drivers'
                                       '\\chromedriver.exe')
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_blazeDemoCompra(self):
        self.driver.get("https://blazedemo.com/")
        self.driver.set_window_size(1936, 1056)
        self.driver.find_element(By.NAME, "fromPort").click()
        dropdown = self.driver.find_element(By.NAME, "fromPort")
        dropdown.find_element(By.XPATH, "//option[. = 'São Paolo']").click()
        self.driver.find_element(By.NAME, "toPort").click()
        dropdown = self.driver.find_element(By.NAME, "toPort")
        dropdown.find_element(By.XPATH, "//option[. = 'Dublin']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "h3").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Flights from São Paolo to Dublin:"
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) .btn").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Your flight from TLV to SFO has been reserved."
        self.driver.find_element(By.ID, "inputName").click()
        self.driver.find_element(By.ID, "inputName").send_keys("Viviane")
        self.driver.find_element(By.CSS_SELECTOR, ".container:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        self.driver.find_element(By.CSS_SELECTOR, "em").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "em").text == "914.76"
        self.driver.find_element(By.ID, "cardType").click()
        dropdown = self.driver.find_element(By.ID, "cardType")
        dropdown.find_element(By.XPATH, "//option[. = 'American Express']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".checkbox").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "Thank you for your purchase today!"

    def test_blazeDemoDestination(self):
        self.driver.get("https://blazedemo.com/")
        self.driver.set_window_size(1296, 1000)
        self.driver.find_element(By.LINK_TEXT, "destination of the week! The Beach!").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        assert self.driver.find_element(By.CSS_SELECTOR,
                                        ".container:nth-child(2)").text == "Destination of the week: Hawaii !"

