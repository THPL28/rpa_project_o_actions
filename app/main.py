import pytest
import os
import sys
from src.core.logger import log

def run():
    """
    Ponto de entrada para execução do framework O-Actions.
    """
    log.info("Iniciando execução do O-Actions Framework...")
    
    # Define argumentos do pytest
    args = [
        "tests",
        "--html=reports/report.html",
        "--self-contained-html",
        "-v"
    ]
    
    # Permite passar argumentos extras via linha de comando
    if len(sys.argv) > 1:
        args.extend(sys.argv[1:])

    # Garante que a pasta de reports existe
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Executa os testes
    exit_code = pytest.main(args)

    if exit_code == 0:
        log.info("Execução finalizada com SUCESSO!")
    else:
        log.warning(f"Execução finalizada com alguns ERROS. Código de saída: {exit_code}")

    log.info(f"Relatório visual gerado em: {os.path.abspath('reports/report.html')}")
    return exit_code

if __name__ == "__main__":
    sys.exit(run())
