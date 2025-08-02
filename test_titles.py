from playwright.sync_api import Page

def test_main_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    page.wait_for_load_state("networkidle")
    
    # Для надежности используйте частичную проверку
    title = page.title()
    assert "Литрес" in title

    assert "электронных и аудиокниг" in title

def test_audiobook_page_title(page: Page):
    page.goto("https://www.litres.ru/")
    page.locator("xpath=//*[@id=\"lowerMenuWrap\"]/nav/div/a[6]").click()
    
    # Выводим фактический title перед проверкой
    actual_title = page.title()
    print(f"\nФактический title страницы: '{actual_title}'")
    
    expect(page).to_have_title("Аудиокниги – слушать онлайн или скачать в mp3 на Литрес")
    page.wait_for_timeout(3000)
   
