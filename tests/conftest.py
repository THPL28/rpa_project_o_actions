import pytest

from src.config import DEFAULT_TIMEOUT, HEADLESS
from src.core.bot import ActionBot


@pytest.fixture(scope="function")
def bot():
    """Provide an ActionBot instance and guarantee driver cleanup."""
    _bot = ActionBot(headless=HEADLESS, timeout=DEFAULT_TIMEOUT)
    yield _bot
    _bot.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot when a UI test fails during its call phase."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    bot = item.funcargs.get("bot")
    if bot is None or getattr(bot, "driver", None) is None:
        return

    try:
        bot.screenshot(f"fail_{item.name}")
    except Exception as exc:  # pragma: no cover - diagnostic fallback
        pytest.fail(f"Falha ao capturar screenshot do teste: {exc}", pytrace=False)
