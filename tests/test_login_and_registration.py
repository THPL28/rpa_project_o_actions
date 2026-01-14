import pytest
from src.page_objects.login_page import LoginPage
from src.page_objects.dashboard_page import DashboardPage
from src.page_objects.registration_page import RegistrationPage
from tests.dados import DATA

def test_login_flow(bot):
    """
    Testa o fluxo de login usando o novo framework O-Actions.
    """
    bot.open('https://parabank.parasoft.com/parabank/index.htm')
    
    login_page = LoginPage(bot)
    login_page.login() # Usa dados padrão de DATA
    
    # Verificação simples (exemplo)
    # assert "Welcome" in bot.get_text("id:loginPanel")

def test_registration_flow(bot):
    """
    Testa o fluxo de registro.
    """
    bot.open('https://parabank.parasoft.com/parabank/index.htm')
    
    dashboard = DashboardPage(bot)
    dashboard.navigate_to_registration()
    
    registration = RegistrationPage(bot)
    registration.register(DATA['register'])

def test_complete_flow(bot):
    """
    Executa o fluxo completo.
    """
    test_login_flow(bot)
    test_registration_flow(bot)


