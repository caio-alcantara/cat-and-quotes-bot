from twilio.twiml.messaging_response import MessagingResponse
from bot_handler import BotHandler 
from message_handlers import QuoteHandler, CatHandler
import os
from dotenv import load_dotenv

load_dotenv()

class MockQuoteService:
    def get_content(self):
        return MockQuote("A famous quote (The Author)", 'text')

class MockCatService:
    def get_content(self):
        return MockCat(os.getenv("CAT_IMG_URL"), 'media')

class MockQuote:
    def __init__(self, content, content_type):
        self.content = content
        self.content_type = content_type

class MockCat:
    def __init__(self, content, content_type):
        self.content = content
        self.content_type = content_type

quote_service = MockQuoteService()
cat_service = MockCatService()

handlers = [
    QuoteHandler(quote_service),
    CatHandler(cat_service)
]

def test_handle_message_only_with_quote(monkeypatch):
    bot_handler = BotHandler(handlers)

    quote_handler_called = []
    def mock_quote_handler_handle(self, message):
        quote_handler_called.append(True)
        quote = quote_service.get_content()
        message.body(quote.content)

    monkeypatch.setattr(QuoteHandler, 'handle', mock_quote_handler_handle)

    response = bot_handler.handle_message('A message with a quote')
    assert quote_handler_called
    assert response == '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>A famous quote (The Author)</Body></Message></Response>'

def test_handle_message_only_with_cat(monkeypatch):
    bot_handler = BotHandler(handlers)

    cat_handler_called = []
    def mock_cat_handler_handle(self, message):
        cat_handler_called.append(True)
        catUrl = cat_service.get_content()
        message.body(catUrl.content)

    monkeypatch.setattr(CatHandler, 'handle', mock_cat_handler_handle)

    response = bot_handler.handle_message('A message with a cat')
    assert cat_handler_called
    assert response == '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>https://cataas.com/cat</Body></Message></Response>'


def test_handle_message_with_both(monkeypatch):
    bot_handler = BotHandler(handlers)

    cat_handler_called = []
    quote_handler_called = []
    def mock_cat_handler_handle(self, message):
        cat_handler_called.append(True)
        catUrl = cat_service.get_content()
        message.body(catUrl.content)

    def mock_quote_handler_handle(self, message):
        quote_handler_called.append(True)
        quote = quote_service.get_content()
        message.body(quote.content)
    
    monkeypatch.setattr(CatHandler, 'handle', mock_cat_handler_handle)
    monkeypatch.setattr(QuoteHandler, 'handle', mock_quote_handler_handle)

    response = bot_handler.handle_message('A message with a cat and a quote')
    assert cat_handler_called
    assert quote_handler_called
    assert response == '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>A famous quote (The Author)</Body><Body>https://cataas.com/cat</Body></Message></Response>'


def test_handle_message_with_neiter():
    bot_handler = BotHandler(handlers)

    cat_handler_called = []
    quote_handler_called = []

    response = bot_handler.handle_message('A message with unrelated text')
    assert not cat_handler_called
    assert not quote_handler_called
    assert response == '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>I only know about famous quotes and cats, sorry!</Body></Message></Response>'