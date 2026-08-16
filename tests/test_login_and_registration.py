import pytest

from src.page_objects.dashboard_page import DashboardPage
from src.page_objects.login_page import LoginPage
from src.page_objects.registration_page import RegistrationPage
from tests.dados import registration_data

BASE_URL = "https://parabank.parasoft.com/parabank/index.htm"


def test_login_flow(bot):
    """Validates that a configured user can sign in and reach the dashboard."""
    bot.open(BASE_URL)
    LoginPage(bot).login()

    assert "Accounts Overview" in bot.get_text("xpath://h1[@class='title']")


def test_registration_flow(bot):
    """Validates registration using unique synthetic test data."""
    bot.open(BASE_URL)
    DashboardPage(bot).navigate_to_registration()

    RegistrationPage(bot).register(registration_data())

    assert "Welcome" in bot.get_text("xpath://h1[@class='title']")


def test_complete_flow(bot):
    """Validates the complete registration flow without nesting pytest tests."""
    bot.open(BASE_URL)
    DashboardPage(bot).navigate_to_registration()
    RegistrationPage(bot).register(registration_data())

    assert "Welcome" in bot.get_text("xpath://h1[@class='title']")
