import pytest

from src.config import DEFAULT_TIMEOUT, HEADLESS
from src.core.bot import ActionBot


@pytest.fixture(scope="function")
def bot():
    """Provide an ActionBot instance and guarantee driver cleanup."""
    browser = ActionBot(headless=HEADLESS, timeout=DEFAULT_TIMEOUT)
    try:
        yield browser
    finally:
        browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot when a UI test fails during its call phase."""
    outcome = yield
    report = outcome.get_result()

    if report.when != "call" or not report.failed:
        return

    browser = item.funcargs.get("bot")
    if browser is None or getattr(browser, "driver", None) is None:
        return

    try:
        browser.screenshot(f"fail_{item.name}")
    except Exception as exc:  # pragma: no cover - diagnostic fallback
        # Diagnostics must never hide the original test failure.
        print(f"Aviso: não foi possível capturar screenshot: {exc}")
