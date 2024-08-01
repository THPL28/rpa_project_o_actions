"""
WaitUtils para funções de espera explícita.

Esta classe define métodos utilitários para esperas explícitas de elementos.

Classes:
    WaitUtils: Utilitário de espera explícita.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    @staticmethod
    def wait_for_element(driver, locator, timeout=10):
        """
        Espera até que um elemento esteja presente na página.

        Args:
            driver (WebDriver): O driver do Selenium WebDriver.
            locator (tuple): Um localizador de elemento (By, value).
            timeout (int): O tempo máximo de espera em segundos.

        Returns:
            WebElement: O elemento encontrado.
        """
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @staticmethod
    def wait_for_element_to_be_clickable(driver, locator, timeout=10):
        """
        Espera até que um elemento esteja clicável na página.

        Args:
            driver (WebDriver): O driver do Selenium WebDriver.
            locator (tuple): Um localizador de elemento (By, value).
            timeout (int): O tempo máximo de espera em segundos.

        Returns:
            WebElement: O elemento encontrado.
        """
        return WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
