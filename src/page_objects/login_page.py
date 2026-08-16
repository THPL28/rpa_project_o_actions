"""Page Object for the ParaBank login page."""

from ..config import TEST_PASSWORD, TEST_USERNAME
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = "name:username"
    PASSWORD_INPUT = "name:password"
    LOGIN_BUTTON = "class:button"
    SUCCESS_MARKER = "id:accountTable"

    def login(self, username: str | None = None, password: str | None = None):
        """Submit credentials supplied explicitly or through environment variables."""
        username = username or TEST_USERNAME
        password = password or TEST_PASSWORD
        if not username or not password:
            raise ValueError("TEST_USERNAME e TEST_PASSWORD devem ser configurados para o teste de login")

        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def is_logged_in(self, timeout: int | None = None) -> bool:
        """Return whether the account page marker is visible after login."""
        try:
            self.wait_for_element(self.SUCCESS_MARKER, timeout=timeout)
            return True
        except Exception:
            return False
