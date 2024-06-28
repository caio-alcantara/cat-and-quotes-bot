from quote_service import QuoteService
import requests
import json

def test_get_quote_returns_quote_in_correct_format(monkeypatch):
    class MockResponse:
        def __init__(self, json_data, status_code=200): ## Adicionei status_code=200
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(*args, **kwargs):
        return MockResponse({"content": "The quote", "author": "The author"}, status_code=200)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "The quote (The author)"
    assert quote.content_type == 'text'


def test_get_quote_handles_http_500(monkeypatch):
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=500)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a quote at this time, sorry."
    assert quote.content_type == f'status code == HTTP500 error'


def test_get_quote_handles_http_400(monkeypatch): ## Bad Request
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=400)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a quote at this time, sorry."
    assert quote.content_type == f'status code == HTTP400 error'


def test_get_quote_handles_http_401(monkeypatch): ## Unauthorized
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=401)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a quote at this time, sorry."
    assert quote.content_type == f'status code == HTTP401 error'


def test_get_quote_handles_http_403(monkeypatch): ## Forbidden
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=403)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a quote at this time, sorry."
    assert quote.content_type == f'status code == HTTP403 error'


def test_get_quote_handles_http_404(monkeypatch): ## Not Found
    class MockResponse:
        def __init__(self, status_code):
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse(status_code=404)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a quote at this time, sorry."
    assert quote.content_type == f'status code == HTTP404 error'


def test_get_quote_handles_missing_content(monkeypatch):
    class MockResponse:
        def __init__(self, json_data, status_code=200):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(*args, **kwargs):
        return MockResponse({"author": "The author"})

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a full quote at this time, sorry."
    assert quote.content_type == 'missing content error'


def test_get_quote_handles_missing_author(monkeypatch):
    class MockResponse:
        def __init__(self, json_data, status_code=200):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    def mock_get(*args, **kwargs):
        return MockResponse({"content": "The quote"})

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a full quote at this time, sorry."
    assert quote.content_type == 'missing content error'


def test_get_quote_handles_extra_fields(monkeypatch):
    class MockResponse:
        def __init__(self, json_data, status_code=200):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data
        
    def mock_get(*args, **kwargs):
        return MockResponse({"content": "The quote", "author": "The author", "tags": ['quote-tag']})

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "The quote (The author)"
    assert quote.content_type == 'text'


def test_get_quote_handles_non_json_response(monkeypatch):
    class MockResponse:
        def __init__(self, text, status_code=200):
            self.text = text
            self.status_code = status_code

        def json(self):
            raise json.JSONDecodeError("Expecting value", self.text, 0)

    def mock_get(*args, **kwargs):
        return MockResponse("<html>This is not JSON</html>", status_code=200)

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "I could not retrieve a quote at this time, sorry."
    assert quote.content_type == 'not json response error'
    

def test_get_quote_handles_timeout(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.exceptions.Timeout("Request timed out")

    monkeypatch.setattr(requests, "get", mock_get)
    quote_service = QuoteService()
    quote = quote_service.get_content()
    assert quote.content == "Request timed out. Could not retrieve a quote at this time, sorry."
    assert quote.content_type == 'requisition timed out error'


## Diversos retornos de erro HTTP (500, 400) -> feito
## Recebe 200, mas não retornou content, só author -> feito
## Recebe 200, mas não retornou author, só content -> feito
## Recebe 200, mas retorna um campo a mais além de content e author -> feito 
## Recebe 200, mas não retorna um json -> feito
## Dá timeout na solicitação -> feito
