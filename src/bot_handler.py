from twilio.twiml.messaging_response import MessagingResponse

class BotHandler:
    def __init__(self, handlers):
        self.handlers = handlers

    def handle_message(self, incoming_msg):
        resp = MessagingResponse()
        message = resp.message()
        message_added = False
        
        for handler in self.handlers:
            if handler.can_handle(incoming_msg):
                handler.handle(message)
              ##  print(resp)
                message_added = True

        if not message_added:
            message.body('I only know about famous quotes and cats, sorry!')
        ##print('resp2', resp)
        return str(resp)

