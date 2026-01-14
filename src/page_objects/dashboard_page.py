"""
DashboardPage para a página inicial após o login.

Esta classe define métodos específicos para interações com a página do dashboard.

Classes:
    DashboardPage: Página do dashboard.
"""

from .base_page import BasePage

class DashboardPage(BasePage):
    REGISTRATION_LINK = "xpath://*[@id='loginPanel']/p[2]/a"

    def navigate_to_registration(self):
        """Navega para a página de registro."""
        self.click(self.REGISTRATION_LINK)
