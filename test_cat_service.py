from cat_service import CatService
import os
from dotenv import load_dotenv

load_dotenv()

def test_get_cat_image_returns_url():
    cat_service = CatService()
    assert cat_service.get_content().content == os.getenv("CAT_IMG_URL")
    assert cat_service.get_content().content_type == 'media'
