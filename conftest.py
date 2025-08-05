from playwright.sync_api import Page
import pytest

@pytest.fixture(autouse=True)  #фикстура предусловие выполнение кода при автоиспользрвани тру, не обязательно прокидывать фикстуру в начале каждого теста 
def open_litres(page: Page):
    page.goto("https://www.litres.ru/")  
    yield page