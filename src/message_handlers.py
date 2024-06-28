from handler_interface import MessageHandler
from twilio.twiml.messaging_response import MessagingResponse

class QuoteHandler(MessageHandler):
    def __init__(self, quote_service):
        self.quote_service = quote_service

    def can_handle(self, incoming_msg: str) -> bool:
        return 'quote' in incoming_msg

    def handle(self, message: MessagingResponse):
        quote = self.quote_service.get_content()
        message.body(quote.content)

class CatHandler(MessageHandler):
    def __init__(self, cat_service):
        self.cat_service = cat_service

    def can_handle(self, incoming_msg: str) -> bool:
        return 'cat' in incoming_msg

    def handle(self, message: MessagingResponse):
        message.media(self.cat_service.get_content().content)
