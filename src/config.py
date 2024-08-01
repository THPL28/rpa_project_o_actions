"""
Configurações do projeto.

Este módulo define as configurações globais do projeto, como o modo de depuração.

Variáveis:
    DEBUG (bool): Indica se o modo de depuração está ativado.
"""
import os


DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'

