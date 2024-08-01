"""
RegistrationPage para a página de registro.

Esta classe define métodos específicos para interações com a página de registro.

Classes:
    RegistrationPage: Página de registro.
"""

from .base_page import BasePage
from selenium.webdriver.common.by import By

class RegistrationPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, 'first_name')
    LAST_NAME_INPUT = (By.ID, 'last_name')
    EMAIL_INPUT = (By.ID, 'email')
    PASSWORD_INPUT = (By.ID, 'password')
    REGISTER_BUTTON = (By.ID, 'register')

    def register(self, first_name, last_name, email, password):
        """
        Realiza o registro de um novo usuário.

        Args:
            first_name (str): O primeiro nome.
            last_name (str): O sobrenome.
            email (str): O e-mail.
            password (str): A senha.
        """
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.EMAIL_INPUT, email)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.REGISTER_BUTTON)
