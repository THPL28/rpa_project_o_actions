"""
ScreenshotUtils para captura de telas.

Esta classe define métodos utilitários para capturar screenshots.

Classes:
    ScreenshotUtils: Utilitário de captura de tela.
"""

import os
import time

class ScreenshotUtils:
    @staticmethod
    def take_screenshot(driver, test_name):
        """
        Captura uma screenshot da tela atual do navegador.

        Args:
            driver (WebDriver): O driver do Selenium WebDriver.
            test_name (str): O nome do teste que está sendo executado.

        Salva a screenshot em um diretório chamado "screenshots" com o nome do teste e um timestamp.
        """
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"{test_name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")
