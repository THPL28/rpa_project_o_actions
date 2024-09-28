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
from tests.dados import DATA

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

def test_login(driver):
    """
    Testa o fluxo de login.

    Realiza o login e verifica se o processo foi bem-sucedido.

    Returns:
        dict: Um dicionário com as chaves 'success', 'msg' e 'retry'.
    """
    try:
        driver.get('https://parabank.parasoft.com/parabank/index.htm')
        
        # Login
        login_page = LoginPage(driver)
        login_page.login(DATA['login'], DATA['password'])
        
        return {'success': True, 'msg': 'ok'}
    except Exception as e:
        if "Unable to locate element" in str(e):
            return {'success': False, 'msg': str(e), 'retry': True}
        else:
            return {'success': False, 'msg': str(e)}


def test_registration(driver):
    """
    Testa o fluxo de registro.

    Realiza o registro de um novo usuário e verifica se o processo foi bem-sucedido.
    """
    try:
        driver.get('https://parabank.parasoft.com/parabank/index.htm')
        
        # Navegar para o Dashboard
        dashboard_page = DashboardPage(driver)
        dashboard_page.navigate_to_registration()
        
        # Registro
        registration_page = RegistrationPage(driver)
        registration_page.register( 
	        DATA['register']['firstname'],
            DATA['register']['lastname'],
            DATA['register']['address'],
            DATA['register']['city'],
            DATA['register']['state'],
            DATA['register']['zipcode'],
            DATA['register']['phone'],
            DATA['register']['ssn'],
            DATA['register']['username'],
            DATA['register']['password'],
            DATA['register']['confirm'],
        )
        return {'success': True, 'msg': 'ok'}
    except Exception as e:
       if "Unable to locate element" in str(e):
            return {'success': False, 'msg': str(e), 'retry': True}
       else:
        return {'success': False, 'msg': str(e)}

def test_login_and_registration(driver):
    """
    Testa o fluxo de login e registro.

    Realiza o login e o registro de um novo usuário e verifica se o processo foi bem-sucedido.
    """
    login_result = test_login(driver)
    registration_result = test_registration(driver)
    if login_result['success'] and registration_result['success']:
        return {'success': True, 'msg': 'Login and registration successful.'}
    else:
        return {'success': False, 'msg': 'Login or registration failed.\n' + login_result['msg'] + '\n' + registration_result['msg']}


