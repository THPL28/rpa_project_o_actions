"""
Testes de login e registro.

Este módulo contém testes para o fluxo de login e registro no site.

Funções:
    test_login_and_registration: Testa o fluxo de login e registro.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from src.page_objects.login_page import LoginPage
from src.page_objects.dashboard_page import DashboardPage
from src.page_objects.registration_page import RegistrationPage
from src.config import DEBUG
from src.utils.screenshot_utils import ScreenshotUtils
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    """
    Fixture para iniciar e finalizar o driver do Selenium.

    Returns:
        WebDriver: O driver do Selenium WebDriver.
    """
    options = Options()
    if DEBUG:
        options.add_experimental_option("detach", True)
        options.add_argument("--auto-open-devtools-for-tabs")
    driver = webdriver.Chrome(options=options)
    yield driver
    if not DEBUG:
        driver.quit()

def test_login_and_registration(driver):
    """
    Testa o fluxo de login e registro.

    Realiza o login, navega para a página de registro e realiza o registro
    de um novo usuário, verificando se o processo foi bem-sucedido.
    """
    try:
        driver.get('https://example.com/login')
        
        # Login
        login_page = LoginPage(driver)
        login_page.login('username', 'password')
        
        # Navegar para o Dashboard
        dashboard_page = DashboardPage(driver)
        dashboard_page.navigate_to_registration()
        
        # Registro
        registration_page = RegistrationPage(driver)
        registration_page.register('First', 'Last', 'email@example.com', 'password')
        
        # Verificação de sucesso
        success_message = driver.find_element(By.ID, 'success_message')
        assert success_message.is_displayed()
    except Exception as e:
        ScreenshotUtils.take_screenshot(driver, 'test_login_and_registration')
        raise e
