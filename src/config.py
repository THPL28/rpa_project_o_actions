import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[1]
load_dotenv(BASE_DIR / ".env")


def _env_bool(name: str, default: bool = False) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        parsed = int(value)
    except ValueError as exc:
        raise ValueError(f"{name} deve ser um inteiro") from exc
    if parsed <= 0:
        raise ValueError(f"{name} deve ser maior que zero")
    return parsed


DEBUG = _env_bool("DEBUG")
HEADLESS = _env_bool("HEADLESS")
DEFAULT_TIMEOUT = _env_int("DEFAULT_TIMEOUT", 10)
BASE_URL = os.getenv("BASE_URL", "https://parabank.parasoft.com/parabank/index.htm")
TEST_USERNAME = os.getenv("TEST_USERNAME")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

LOGS_DIR = BASE_DIR / "logs"
REPORTS_DIR = BASE_DIR / "reports"
SCREENSHOTS_DIR = BASE_DIR / "screenshots"
