from cat_service import CatService

def test_get_cat_image_returns_url():
    cat_service = CatService()
    assert cat_service.get_content().content == 'https://cataas.com/cat'
    assert cat_service.get_content().content_type == 'media'
