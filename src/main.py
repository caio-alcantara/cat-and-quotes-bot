from flask import Flask, request
from cat_service import CatService
from quote_service import QuoteService
from bot_handler import BotHandler

quote_service = QuoteService()
cat_service = CatService()
bot_handler = BotHandler(quote_service, cat_service)

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = bot_handler.handle_message(incoming_msg)
    return response

if __name__ == '__main__':
    app.run(port=4000)
