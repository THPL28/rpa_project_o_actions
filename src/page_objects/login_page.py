"""
LoginPage para a página de login.

Esta classe define métodos específicos para interações com a página de login.

Classes:
    LoginPage: Página de login.
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login')

    def login(self, username, password):
        """
        Realiza o login no sistema.

        Args:
            username (str): O nome de usuário.
            password (str): A senha.
        """
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
