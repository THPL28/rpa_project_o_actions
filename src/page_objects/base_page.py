"""Shared Page Object helpers."""

from ..core.bot import ActionBot


class BasePage:
    def __init__(self, bot: ActionBot):
        self.bot = bot

    def enter_text(self, locator, text: str):
        self.bot.type(locator, text)
        return self

    def click(self, locator):
        self.bot.click(locator)
        return self

    def wait_for_element(self, locator, timeout: int | None = None):
        return self.bot.find(locator, timeout=timeout)

    def get_text(self, locator) -> str:
        return self.bot.get_text(locator)

    def screenshot(self, prefix: str = "page") -> str:
        return self.bot.screenshot(prefix)
