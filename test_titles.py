from playwright.sync_api import Page

def test_main_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    page.wait_for_load_state("networkidle")
    
    # Для надежности используйте частичную проверку
    title = page.title()
    assert "Литрес" in title
    assert "электронных и аудиокниг" in title