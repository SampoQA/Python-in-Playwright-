from playwright.sync_api import Page, expect

def test_main_action(page: Page):
    page.get_by_test_id("search__input").fill("python")
    page.keyboard.press("Enter")
    
    expect(page).to_have_url("https://www.litres.ru/search/?q=python")
    page.locator("xpath=//*[@aria-description='Книги, которые можно читать без ограничений с активной Литрес: Подпиской']").dblclick()
    page.locator("xpath=//*[@aria-description='Книги, которые можно взять по Литрес: Абонементу']").click()

    #page.get_by_label("Русский").check() #скрытый элемент уязвимость для теста 
    #page.locator("xpath=//[*id='languages-ru']").click(force=True) #глючит force=True - принудительная работа теста 
    page.check("label[for='languages-ru']")

    page.locator("button:has-text('Принять')").click() #по умоляанию использует css - локаторы это строчка помогает принять запись куков

    #page.screenshot(path="../screenshoot/action.png") #сохраняет в папку выше скрииншот и создает папку если её нет 
    page.pause() #делает остановку в конце теста и показывает чем все закончилось запускаеться в headed режиме 

