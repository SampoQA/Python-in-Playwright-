# Импорт необходимых модулей из библиотеки Playwright
# Page - класс для управления браузерной страницей
# expect - функция для утверждений (assertions) в тестах
from playwright.sync_api import Page, expect
 
def test_locator_role(page: Page):  # Объявление тестовой функции test_locator_role; page: Page - экземпляр класса Page, передается как аргумент функции

    page.goto("https://www.litres.ru/")     # Вызов метода goto() у объекта page - переход на указанный URL
    page.get_by_role("button", name="Найти").click()  # Поиск элемента с ролью "button" и текстом "Найти", затем клик по нему
    expect(page.get_by_text("стивен кинг")).to_be_visible()  # Ожидание, что текст "стивен кинг" становится видимым


def test_locator_placeholder(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_placeholder("Искать на Литрес").fill("игра престолов")  # Поиск элемента с плейсхолдером "Искать на Литрес" и ввод текста "игра престолов"
    page.keyboard.press("Enter") # Нажатие клавиши Enter для отправки запроса
    expect(page.get_by_text("Результаты поиска «игра престолов»")).to_be_visible() # Ожидание, что текст "Результаты поиска «игра престолов»" становится видимым

def test_locator_placeholder_datatestid(page: Page):
    page.goto("https://www.litres.ru/")
    page.get_by_test_id("header-catalog-button").click()  # Поиск элемента с test-id "header-catalog-button" и клик по нему
    expect(page.get_by_text("Бесплатные книги")).to_be_visible()  # Ожидание, что текст "Бесплатные книги" становится видимым

def test_locator_alt(page:Page):
    page.goto("https://www.litres.ru/audiobooks/")
    page.get_by_alt_text("Логотип Литрес").click()  # Поиск элемента с атрибутом alt "Логотип Литрес" и клик по нему
    expect(page).to_have_url("https://www.litres.ru/")  # Ожидание, что URL страницы соответствует указанному значению

def test_locator_xpath(page: Page):
    page.goto("https://www.litres.ru/")
    expect(page.locator("xpath=//a[@title='YouTube']")).to_be_visible()  # Ожидание, что элемент с заголовком "YouTube" становится видимым

