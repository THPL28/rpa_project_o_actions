import pytest
import os
from src.core.bot import ActionBot
from src.config import HEADLESS, DEFAULT_TIMEOUT

@pytest.fixture(scope="function")
def bot():
    """
    Fixture que fornece uma instância do ActionBot para os testes.
    """
    _bot = ActionBot(headless=HEADLESS, timeout=DEFAULT_TIMEOUT)
    yield _bot
    _bot.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Executa o hook padrão
    outcome = yield
    report = outcome.get_result()

    # Se o teste falhar, tira uma screenshot se o bot estiver disponível
    if report.when == "call" and report.failed:
        if "bot" in item.funcargs:
            bot = item.funcargs["bot"]
            screenshot_path = bot.screenshot(f"fail_{item.name}")
            # Aqui poderíamos anexar ao report do pytest-html se configurado
