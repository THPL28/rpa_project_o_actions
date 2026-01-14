from src.core.bot import ActionBot
from src.core.logger import log

def simple_automation():
    # Inicializa o bot (pode ser usado fora do pytest também)
    bot = ActionBot(headless=False)
    
    try:
        # Sintaxe ultra simples e intuitiva
        bot.open("https://www.google.com")
        
        # Uso de locatários inteligentes (Name, ID, XPath, etc via strings)
        bot.type("name:q", "O-Actions RPA Framework")
        bot.wait(1)
        
        bot.screenshot("google_search")
        log.info("Execução de exemplo concluída com sucesso!")
        
    except Exception as e:
        log.error(f"Erro na automação: {e}")
    finally:
        bot.quit()

if __name__ == "__main__":
    simple_automation()
