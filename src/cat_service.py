from service_response import ServiceResponse
import os
from dotenv import load_dotenv

load_dotenv()

class CatService:
    def get_content(self):
        return ServiceResponse(os.getenv("CAT_IMG_URL"), 'media')