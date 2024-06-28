from abc import ABC, abstractmethod
from twilio.twiml.messaging_response import MessagingResponse

## Contrato / Template para criação de novos handlers 

class MessageHandler(ABC):
    @abstractmethod
    def can_handle(self, incoming_msg: str) -> bool:
        pass

    @abstractmethod
    def handle(self, message: MessagingResponse):
        pass
