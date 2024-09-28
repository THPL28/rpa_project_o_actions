import pytest
import os

# Executa os testes
exec_code = pytest.main()

# Verifica se o relatório foi gerado
if exec_code == 0:
    print("Todos os testes passaram!")
else:
    print("Alguns testes falharam.")

# Informa sobre o relatório gerado
report_path = os.path.join(os.getcwd(), "report.html")
print(f"Relatório de testes gerado em: {report_path}")
