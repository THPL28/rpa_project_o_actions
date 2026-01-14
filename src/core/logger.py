import sys
import os
from loguru import logger

def setup_logger():
    """
    Configura o logger para o framework O-Actions.
    Logs são salvos na pasta 'logs' na raiz do projeto.
    """
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Remove o logger padrão do loguru (que vai para stderr)
    logger.remove()

    # Adiciona logger para o console com cores e formato atraente
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )

    # Adiciona logger para arquivo
    logger.add(
        os.path.join(log_dir, "bot_{time}.log"),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG",
        rotation="10 MB",
        retention="10 days"
    )

    return logger

# Instância global do logger para fácil acesso
log = setup_logger()
