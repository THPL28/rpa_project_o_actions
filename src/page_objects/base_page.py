"""
BasePage para interações comuns com páginas da web.

Esta classe define métodos comuns para interação com elementos da página,
como clicar, entrar texto e esperar elementos.

Classes:
    BasePage: Classe base para todas as páginas.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """
        Inicializa a BasePage com o driver do Selenium.

        Args:
            driver (WebDriver): O driver do Selenium WebDriver.
        """
        self.driver = driver

    def enter_text(self, locator, text):
        """
        Insere texto em um campo de entrada.

        Args:
            locator (tuple): Um localizador de elemento (By, value).
            text (str): O texto a ser inserido.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def click(self, locator):
        """
        Clica em um elemento.

        Args:
            locator (tuple): Um localizador de elemento (By, value).
        """
        element = self.wait_for_element(locator)
        element.click()

    def wait_for_element(self, locator, timeout=10):
        """
        Espera até que um elemento esteja presente na página.

        Args:
            locator (tuple): Um localizador de elemento (By, value).
            timeout (int): O tempo máximo de espera em segundos.

        Returns:
            WebElement: O elemento encontrado.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def get_element(self, locator):
        """
        Obtém um elemento presente na página.

        Args:
            locator (tuple): Um localizador de elemento (By, value).

        Returns:
            WebElement: O elemento encontrado.
        """
        return self.wait_for_element(locator)

    def get_text(self, locator):
        """
        Obtém o texto de um elemento.

        Args:
            locator (tuple): Um localizador de elemento (By, value).

        Returns:
            str: O texto do elemento.
        """
        element = self.wait_for_element(locator)
        return element.text
