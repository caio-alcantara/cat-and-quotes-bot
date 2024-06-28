from twilio.twiml.messaging_response import MessagingResponse

class BotHandler:
    def __init__(self, quote_service, cat_service):
        self.quote_service = quote_service
        self.cat_service = cat_service

    def handle_message(self, incoming_msg):
        resp = MessagingResponse()
        msg = resp.message()
        responded = False
        if 'quote' in incoming_msg:
            quote = self.quote_service.get_content()
            msg.body(quote.content)
            responded = True
        if 'cat' in incoming_msg:
            cat_image_url = self.cat_service.get_content()
            msg.media(cat_image_url.content)
            responded = True
        if not responded:
            msg.body('I only know about famous quotes and cats, sorry!')
        return str(resp)
