import os
import time
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from .logger import log


class ActionBot:
    """Small, explicit abstraction over Selenium WebDriver."""

    _LOCATOR_MAP = {
        "id": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH,
        "css": By.CSS_SELECTOR,
        "class": By.CLASS_NAME,
        "text": By.LINK_TEXT,
        "partial_text": By.PARTIAL_LINK_TEXT,
        "tag": By.TAG_NAME,
    }

    def __init__(self, driver=None, headless=False, timeout=10):
        if timeout <= 0:
            raise ValueError("timeout deve ser maior que zero")

        self.timeout = timeout
        self.driver = driver or self._setup_driver(headless)
        log.info("ActionBot inicializado")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.quit()
        return False

    def _setup_driver(self, headless):
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service, options=chrome_options)

    def open(self, url):
        if not url or not url.strip():
            raise ValueError("url não pode ser vazia")
        log.info("Navegando para: %s", url)
        self.driver.get(url)
        return self

    def find(self, locator, timeout=None, clickable=False):
        """Find an element using a tuple or an explicit smart-locator string."""
        wait_timeout = self.timeout if timeout is None else timeout
        if wait_timeout <= 0:
            raise ValueError("timeout deve ser maior que zero")

        parsed = self._parse_locator(locator)
        condition = (
            EC.element_to_be_clickable(parsed)
            if clickable
            else EC.presence_of_element_located(parsed)
        )

        try:
            return WebDriverWait(self.driver, wait_timeout).until(condition)
        except TimeoutException:
            log.error("Timeout ao localizar elemento: %s", locator)
            self.screenshot(f"fail_find_{int(time.time())}")
            raise

    def click(self, locator):
        self.find(locator, clickable=True).click()
        return self

    def type(self, locator, text, clear=True):
        element = self.find(locator, clickable=True)
        if clear:
            element.clear()
        # Never log the actual value typed: it may contain credentials or PII.
        log.debug("Preenchendo campo: %s", locator)
        element.send_keys(text)
        return self

    def get_text(self, locator):
        return self.find(locator).text

    def wait(self, seconds):
        """Explicit sleep kept for exceptional cases; prefer condition-based waits."""
        if seconds < 0:
            raise ValueError("seconds não pode ser negativo")
        log.warning("Sleep explícito de %s segundos; prefira waits condicionais", seconds)
        time.sleep(seconds)
        return self

    def screenshot(self, filename=None):
        filename = filename or f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs("screenshots", exist_ok=True)
        path = os.path.join("screenshots", f"{filename}.png")
        self.driver.save_screenshot(path)
        log.info("Screenshot salva em: %s", path)
        return path

    @classmethod
    def _parse_locator(cls, locator):
        if isinstance(locator, tuple):
            if len(locator) != 2:
                raise ValueError("locator tuple deve conter (By, value)")
            return locator

        if not isinstance(locator, str) or not locator.strip():
            raise ValueError("locator deve ser uma string não vazia ou uma tupla (By, value)")

        prefix, separator, value = locator.partition(":")
        if separator:
            by = cls._LOCATOR_MAP.get(prefix.lower().strip())
            if by is None:
                raise ValueError(
                    f"Prefixo de locator desconhecido: '{prefix}'. "
                    f"Use: {', '.join(cls._LOCATOR_MAP)}"
                )
            if not value.strip():
                raise ValueError("valor do locator não pode ser vazio")
            return by, value

        # Backwards-compatible default: an unprefixed locator is an element id.
        return By.ID, locator

    def quit(self):
        if getattr(self, "driver", None) is not None:
            log.info("Encerrando ActionBot")
            self.driver.quit()
            self.driver = None
