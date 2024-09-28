"""
LoginPage para a página de login.

Esta classe define métodos específicos para interações com a página de login.

Classes:
    LoginPage: Página de login.
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By
from tests.dados import DATA

class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH,  '//*[@id="loginPanel"]/form/div[1]/input')
    PASSWORD_INPUT   = (By.NAME, 'password')
    LOGIN_BUTTON  = (By.CLASS_NAME, 'button')

    def login(self, username, password):
        """
        Realiza o login no sistema.

        Args:
            username (str): O nome de usuário.
            password (str): A senha.
        """
        self.enter_text(self.USERNAME_INPUT, DATA['login'])
        self.enter_text(self.PASSWORD_INPUT, DATA['password'])
        self.click(self.LOGIN_BUTTON)
