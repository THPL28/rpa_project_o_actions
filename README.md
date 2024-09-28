<<<<<<< HEAD
# RPA Project with Selenium and Event-Driven Architecture

## 📚 Introdução

Este projeto é uma automação de teste usando Selenium com uma arquitetura orientada a eventos. O projeto utiliza o padrão de Page Object Model para separar a lógica de interação com a página da lógica de teste, e é configurado para executar testes tanto em modo de produção quanto em modo de depuração.

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.10**: Linguagem de programação usada para escrever o projeto.
- **Selenium**: Biblioteca para controle de browsers e automação de testes.
- **pytest**: Framework para testes de unidade e integração.
- **ChromeDriver**: Driver do Selenium para o Google Chrome.
- **pyee**: Biblioteca para eventos, usada para a arquitetura orientada a eventos.
- **dotenv**: Carregamento de variáveis de ambiente de arquivos `.env`.

## 📦 Requisitos

Certifique-se de ter o Python 3.10 ou superior instalado. Instale as dependências do projeto com o comando abaixo:

pip install -r requirements.txt



##  📁 Estrutura do Projeto

rpa_project_o_actions/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── event_handler.py
│   ├── page_objects/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── dashboard_page.py
│   │   ├── registration_page.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── wait_utils.py
│   │   ├── screenshot_utils.py
├── tests/
│   ├── __init__.py
│   ├── test_login_and_registration.py
├── requirements.txt
└── README.md


src/: Contém a lógica de automação e as definições das páginas.

tests/: Contém os testes automatizados.
requirements.txt: Lista as dependências do projeto.

##  🚀 Configuração e Execução

##  Configuração
Instale as dependências:

pip install -r requirements.txt
Defina variáveis de ambiente:

DEBUG: Se true, o navegador será executado em modo de depuração e não será fechado automaticamente. Para definir:

# No Windows:
set DEBUG=true

# No Linux/macOS:
export DEBUG=true
## Configure o PYTHONPATH:

# No Windows:
set PYTHONPATH=%CD%\src

# No Linux/macOS:
export PYTHONPATH=$(pwd)/src

## Executar Testes
Para executar os testes, use o comando:
pytest

Isso executará todos os testes localizados no diretório tests/.

## Modo de Depuração
Para executar o navegador no modo de depuração, defina a variável de ambiente DEBUG como true. O navegador será executado com as ferramentas de desenvolvedor abertas.

## 📝 Documentação das Classes e Métodos
src/config.py
Define configurações globais, como o modo de depuração.

src/page_objects/base_page.py
Classe base para interações comuns com elementos da página.

# Métodos:
enter_text(locator, text): Insere texto em um campo.
click(locator): Clica em um elemento.
wait_for_element(locator, timeout): Espera até que um elemento esteja presente.
src/page_objects/login_page.py
Define métodos específicos para a página de login.

login(username, password): Realiza o login.
src/page_objects/dashboard_page.py
Define métodos específicos para a página do dashboard.

navigate_to_registration(): Navega para a página de registro.
src/page_objects/registration_page.py
Define métodos específicos para a página de registro.

register(first_name, last_name, email, password): Realiza o registro de um novo usuário.
src/utils/wait_utils.py
Métodos utilitários para esperas explícitas de elementos.

src/utils/screenshot_utils.py
Métodos utilitários para captura de screenshots.

## 🧪 Testes
O projeto inclui testes automatizados para o fluxo de login e registro. Eles estão localizados no arquivo tests/test_login_and_registration.py. Estes testes verificam a funcionalidade de login, navegação e registro no site.

## 📜 Contribuição
Contribuições são bem-vindas! Para contribuir, por favor:

Faça um fork deste repositório.
Crie uma branch para sua feature (git checkout -b minha-feature).
Faça commit das suas mudanças (git commit -am 'Adiciona nova feature').
Faça um push para a branch (git push origin minha-feature).
## Abra um Pull Request.
=======
# RPA Project with Selenium and Event-Driven Architecture

## 📚 Introdução

Este projeto é uma automação de teste usando Selenium com uma arquitetura orientada a eventos. O projeto utiliza o padrão de Page Object Model para separar a lógica de interação com a página da lógica de teste, e é configurado para executar testes tanto em modo de produção quanto em modo de depuração.

## 🛠️ Tecnologias e Bibliotecas

- **Python 3.10**: Linguagem de programação usada para escrever o projeto.
- **Selenium**: Biblioteca para controle de browsers e automação de testes.
- **pytest**: Framework para testes de unidade e integração.
- **ChromeDriver**: Driver do Selenium para o Google Chrome.
- **pyee**: Biblioteca para eventos, usada para a arquitetura orientada a eventos.
- **dotenv**: Carregamento de variáveis de ambiente de arquivos `.env`.

## 📦 Requisitos

Certifique-se de ter o Python 3.10 ou superior instalado. Instale as dependências do projeto com o comando abaixo:

pip install -r requirements.txt



##  📁 Estrutura do Projeto
```plaintext
rpa_project_o_actions/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── event_handler.py
│   ├── page_objects/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── dashboard_page.py
│   │   ├── registration_page.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── wait_utils.py
│   │   ├── screenshot_utils.py
├── tests/
│   ├── __init__.py
│   ├── test_login_and_registration.py
├── requirements.txt
└── README.md

````
src/: Contém a lógica de automação e as definições das páginas.

tests/: Contém os testes automatizados.
requirements.txt: Lista as dependências do projeto.

##  🚀 Configuração e Execução

##  Configuração
Instale as dependências:

pip install -r requirements.txt
Defina variáveis de ambiente:

DEBUG: Se true, o navegador será executado em modo de depuração e não será fechado automaticamente. Para definir:

# No Windows:
set DEBUG=true

# No Linux/macOS:
export DEBUG=true
## Configure o PYTHONPATH:

# No Windows:
set PYTHONPATH=%CD%\src

# No Linux/macOS:
export PYTHONPATH=$(pwd)/src

## Executar Testes
Para executar os testes, use o comando:
pytest

Isso executará todos os testes localizados no diretório tests/.

## Modo de Depuração
Para executar o navegador no modo de depuração, defina a variável de ambiente DEBUG como true. O navegador será executado com as ferramentas de desenvolvedor abertas.

## 📝 Documentação das Classes e Métodos
src/config.py
Define configurações globais, como o modo de depuração.

src/page_objects/base_page.py
Classe base para interações comuns com elementos da página.

# Métodos:
enter_text(locator, text): Insere texto em um campo.
click(locator): Clica em um elemento.
wait_for_element(locator, timeout): Espera até que um elemento esteja presente.
src/page_objects/login_page.py
Define métodos específicos para a página de login.

login(username, password): Realiza o login.
src/page_objects/dashboard_page.py
Define métodos específicos para a página do dashboard.

navigate_to_registration(): Navega para a página de registro.
src/page_objects/registration_page.py
Define métodos específicos para a página de registro.

register(first_name, last_name, email, password): Realiza o registro de um novo usuário.
src/utils/wait_utils.py
Métodos utilitários para esperas explícitas de elementos.

src/utils/screenshot_utils.py
Métodos utilitários para captura de screenshots.

## 🧪 Testes
O projeto inclui testes automatizados para o fluxo de login e registro. Eles estão localizados no arquivo tests/test_login_and_registration.py. Estes testes verificam a funcionalidade de login, navegação e registro no site.

## 📜 Contribuição
Contribuições são bem-vindas! Para contribuir, por favor:

Faça um fork deste repositório.
Crie uma branch para sua feature (git checkout -b minha-feature).
Faça commit das suas mudanças (git commit -am 'Adiciona nova feature').
Faça um push para a branch (git push origin minha-feature).
## Abra um Pull Request.
>>>>>>> 9412045a74aa92616a25a87bdd517269f797c92a
