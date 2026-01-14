import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from .logger import log

class ActionBot:
    def __init__(self, driver=None, headless=False, timeout=10):
        self.timeout = timeout
        if driver:
            self.driver = driver
        else:
            self.driver = self._setup_driver(headless)
        
        log.info("ActionBot inicializado.")

    def _setup_driver(self, headless):
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        
        # Otimizações básicas
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver

    def open(self, url):
        log.info(f"Navegando para: {url}")
        self.driver.get(url)

    def find(self, locator, timeout=None):
        """
        Encontra um elemento usando um localizador inteligente ou tupla (By, value).
        """
        t = timeout or self.timeout
        try:
            return WebDriverWait(self.driver, t).until(
                EC.presence_of_element_located(self._parse_locator(locator))
            )
        except TimeoutException:
            log.error(f"Timeout ao tentar encontrar elemento: {locator}")
            self.screenshot(f"fail_find_{int(time.time())}")
            raise

    def click(self, locator):
        element = self.find(locator)
        log.debug(f"Clicando em: {locator}")
        element.click()

    def type(self, locator, text, clear=True):
        element = self.find(locator)
        log.debug(f"Digitando '{text}' em: {locator}")
        if clear:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find(locator)
        return element.text

    def wait(self, seconds):
        log.debug(f"Esperando {seconds} segundos...")
        time.sleep(seconds)

    def screenshot(self, filename=None):
        if not filename:
            filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        path = os.path.join("screenshots", f"{filename}.png")
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        
        self.driver.save_screenshot(path)
        log.info(f"Screenshot salva em: {path}")
        return path

    def _parse_locator(self, locator):
        """
        Converte strings intuitivas em locators do Selenium.
        Ex: "id:loginButton" -> (By.ID, "loginButton")
        """
        if isinstance(locator, tuple):
            return locator
        
        if ":" in locator:
            prefix, value = locator.split(":", 1)
            prefix = prefix.lower().strip()
            if prefix == "id": return (By.ID, value)
            if prefix == "name": return (By.NAME, value)
            if prefix == "xpath": return (By.XPATH, value)
            if prefix == "css": return (By.CSS_SELECTOR, value)
            if prefix == "class": return (By.CLASS_NAME, value)
            if prefix == "text": return (By.LINK_TEXT, value)
        
        # Default para CSS se não houver prefixo claro mas parecer CSS, ou ID por padrão
        return (By.ID, locator)

    def quit(self):
        log.info("Encerrando ActionBot.")
        self.driver.quit()
