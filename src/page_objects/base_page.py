from ..core.bot import ActionBot
from ..core.logger import log

class BasePage:
    def __init__(self, bot: ActionBot):
        """
        Inicializa a BasePage com o ActionBot.
        """
        self.bot = bot
        self.driver = bot.driver # Mantido para compatibilidade se necessário

    def enter_text(self, locator, text):
        """Insere texto em um campo."""
        self.bot.type(locator, text)

    def click(self, locator):
        """Clica em um elemento."""
        self.bot.click(locator)

    def wait_for_element(self, locator, timeout=None):
        """Espera por um elemento."""
        return self.bot.find(locator, timeout=timeout)

    def get_text(self, locator):
        """Retorna o texto de um elemento."""
        return self.bot.get_text(locator)
    
    def screenshot(self, prefix="page"):
        """Captura uma screenshot."""
        self.bot.screenshot(prefix)
