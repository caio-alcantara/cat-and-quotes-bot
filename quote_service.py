import requests
import json
from service_response import ServiceResponse
import os
from dotenv import load_dotenv

load_dotenv()


class QuoteService:
    def get_content(self):
        try:
            r = requests.get(os.getenv("QUOTE_API_URL"), timeout=5)  # Timeout 5
        except requests.exceptions.Timeout:
            return ServiceResponse('Request timed out. Could not retrieve a quote at this time, sorry.', 'requisition timed out error')
        
        if r.status_code != 200:
            return ServiceResponse('I could not retrieve a quote at this time, sorry.', f'status code == HTTP{r.status_code} error')
        
        try:
            data = r.json()
        except json.JSONDecodeError:
            return ServiceResponse('I could not retrieve a quote at this time, sorry.', 'not json response error')
        
        if 'content' not in data or 'author' not in data:
            return ServiceResponse('I could not retrieve a full quote at this time, sorry.', 'missing content error')
        
        quote = Quote(data['content'], data['author'])
        return ServiceResponse(str(quote), 'text')        
    
class Quote:
    def __init__(self, content, author):
        self.content = content
        self.author = author

    def __str__(self):
        return f'{self.content} ({self.author})'
