# O-Actions RPA Framework 🤖✨

**O-Actions** é um framework de automação de processos robóticos (RPA) moderno e de alta performance, construído sobre o Selenium, projetado para ser intuitivo, robusto e fácil de manter.

## 🚀 Principais Recursos

- **ActionBot Engine**: Comando simplificados e intuitivos (ex: `bot.click("id:login")`).
- **Smart Locators**: Suporte a seletores inteligentes via strings (ID, Name, XPath, CSS, Text).
- **Auto-Wait**: Gerenciamento automático de espera sincronizada para evitar "flaky tests".
- **Logging de Elite**: Integração total com `loguru` para rastreamento visual e em arquivo.
- **Reporting Visual**: Geração de relatórios HTML detalhados com screenshots integrados.
- **Page Object Pattern**: Implementação otimizada para máxima reutilização de código.

## 🛠️ Instalação

Certifique-se de ter o Python 3.8+ instalado.

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/rpa_project_o_actions.git

# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Ou: venv\Scripts\activate no Windows

# Instale as dependências
pip install -r requirements.txt
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto:

```env
DEBUG=true
HEADLESS=false
DEFAULT_TIMEOUT=15
```

## 📋 Como Usar

### Executando a Suite Completa
Para rodar todos os testes e gerar o relatório HTML:

```bash
python app/main.py
```

O relatório será gerado em `reports/report.html`.

### Exemplo de Automação Rápida
Veja como a sintaxe é limpa:

```python
from src.core.bot import ActionBot

bot = ActionBot()
bot.open("https://www.google.com")
bot.type("name:q", "O-Actions RPA")
bot.screenshot("google_search")
bot.quit()
```

## 📁 Estrutura do Projeto

- `src/core/`: O coração do framework (ActionBot e Logger).
- `src/page_objects/`: Definições de telas e componentes.
- `src/utils/`: Utilitários de reporte e capturas.
- `app/`: Ponto de entrada da aplicação.
- `tests/`: Suite de testes automatizados.
- `examples/`: Exemplos práticos de uso do framework.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---
Desenvolvido por [Seu Nome/Empresa]
