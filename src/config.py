import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
HEADLESS = os.getenv('HEADLESS', 'false').lower() == 'true'
DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', 10))

# Definições de caminhos
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOGS_DIR = os.path.join(BASE_DIR, "logs")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(BASE_DIR, "screenshots")
