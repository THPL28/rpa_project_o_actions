"""
LoginPage para a página de login.

Esta classe define métodos específicos para interações com a página de login.

Classes:
    LoginPage: Página de login.
"""

from .base_page import BasePage
from tests.dados import DATA

class LoginPage(BasePage):
    USERNAME_INPUT = "xpath://*[@id='loginPanel']/form/div[1]/input"
    PASSWORD_INPUT = "name:password"
    LOGIN_BUTTON   = "class:button"

    def login(self, username=None, password=None):
        """Realiza o login no sistema."""
        u = username or DATA['login']
        p = password or DATA['password']
        
        self.enter_text(self.USERNAME_INPUT, u)
        self.enter_text(self.PASSWORD_INPUT, p)
        self.click(self.LOGIN_BUTTON)
