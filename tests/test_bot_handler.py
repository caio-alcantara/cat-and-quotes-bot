from twilio.twiml.messaging_response import MessagingResponse
from bot_handler import BotHandler  # substitua 'bot_handler' pelo nome do módulo onde BotHandler está definido
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

def test_handle_message_only_with_quote(monkeypatch):
    mock_quote_service = MockQuoteService()
    mock_cat_service = MockCatService()

    bot_handler = BotHandler(mock_quote_service, mock_cat_service)

    quote_service_called = []

    def mock_get_quote_content():
        quote_service_called.append(True)
        return MockQuote("A famous quote (The Author)", 'text')

    monkeypatch.setattr(mock_quote_service, 'get_content', mock_get_quote_content)

    response = bot_handler.handle_message("Tell me a quote")
    assert quote_service_called
    assert response == '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>A famous quote (The Author)</Body></Message></Response>'

def test_handle_message_only_with_cat(monkeypatch):
    mock_quote_service = MockQuoteService()
    mock_cat_service = MockCatService()

    bot_handler = BotHandler(mock_quote_service, mock_cat_service)

    cat_service_called = []

    def mock_get_cat_content():
        cat_service_called.append(True)
        return MockCat(os.getenv("CAT_IMG_URL"), 'media')
    
    monkeypatch.setattr(mock_cat_service, 'get_content', mock_get_cat_content)

    response = bot_handler.handle_message('Show me a cat picture')
    assert cat_service_called
    assert response == f'<?xml version="1.0" encoding="UTF-8"?><Response><Message><Media>{os.getenv("CAT_IMG_URL")}</Media></Message></Response>'

def test_handle_message_with_both(monkeypatch):
    mock_quote_service = MockQuoteService()
    mock_cat_service = MockCatService()

    bot_handler = BotHandler(mock_quote_service, mock_cat_service)

    cat_service_called = []
    quote_service_called = []

    def mock_get_quote_content():
        quote_service_called.append(True)
        return MockQuote("A famous quote (The Author)", 'text')

    def mock_get_cat_content():
        cat_service_called.append(True)
        return MockCat(os.getenv("CAT_IMG_URL"), 'media')
    
    monkeypatch.setattr(mock_quote_service, 'get_content', mock_get_quote_content)
    monkeypatch.setattr(mock_cat_service, 'get_content', mock_get_cat_content)

    response = bot_handler.handle_message('Show me a cat and a quote')
    assert cat_service_called
    assert quote_service_called
    assert response == f'<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>A famous quote (The Author)</Body><Media>{os.getenv("CAT_IMG_URL")}</Media></Message></Response>'

def test_handle_message_with_neiter(monkeypatch):
    mock_quote_service = MockQuoteService()
    mock_cat_service = MockCatService()

    bot_handler = BotHandler(mock_quote_service, mock_cat_service)

    cat_service_called = []
    quote_service_called = []

    def mock_get_quote_content():
        quote_service_called.append(True)
        return MockQuote("A famous quote", 'text')

    def mock_get_cat_content():
        cat_service_called.append(True)
        return MockCat(os.getenv("CAT_IMG_URL"), 'media')
    
    monkeypatch.setattr(mock_quote_service, 'get_content', mock_get_quote_content)
    monkeypatch.setattr(mock_cat_service, 'get_content', mock_get_cat_content)

    response = bot_handler.handle_message('Unrelated text')
    assert not cat_service_called
    assert not quote_service_called
    assert response == '<?xml version="1.0" encoding="UTF-8"?><Response><Message><Body>I only know about famous quotes and cats, sorry!</Body></Message></Response>'
