'''Event Handler: Sistema de eventos para reagir a ações específicas.'''
# src/event_handler.py
from pyee import BaseEventEmitter

class EventHandler(BaseEventEmitter):
    '''
    EventHandler: Classe que herda de BaseEventEmitter do pyee, permitindo a definição e emissão de eventos.
    event_handler: Instância de EventHandler usada para gerenciar eventos no projeto.
    '''
    def __init__(self):
        super().__init__()
   
event_handler = EventHandler()

