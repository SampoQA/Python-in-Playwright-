Playwright

playwright codegen (url) Инспектор кода может, записывая действия создавать код для теста 

-обязательно сохранять каждое изменение 
Важно имя теста test_

важные команды через консоль

Запуск всей папки pytest --headed --debug

запуск отдельного файла  переход в папку cd tests

запуск видимо и с дебагом  pytest --headed --debug (--ui)
запуск отдельного теста  из файла    pytest test_locators.py::test_locator_placeholder --headed
Переход в конкретную папку cd tests
Возврат на директорию выше cd ..
создание папки md
содержимое папки ls

    yield page использовать аккуратно так как без него редакторы не подтягивает остальные объекты поэтому обязательно использовать (page: Page Ex - def open_litres(page: Page):
CLI - Интерфейс командной строки (англ. Command Line Interface, CLI). Передавая различные параметры в командной строке, вы можете менять поведение в работе playwright.

Рассмотрим подробнее команды для управления playwright с помощью cli

--headed - playwright по умолчанию запускает браузеры в безголовом(headless) режиме. При использовании данного аргумента, запуск теста произойдет в режиме headed.

--browser - запускать тесты в другом браузере chromium, firefox или webkit. Может быть указано несколько раз (по умолчанию: chromium).

pytest --headed --browser webkit --browser firefox
--browser-channel - возможно вам потребуется запускать тесты в браузерах  Chrome и Edge, установленных на вашем компьютере.

pytest --browser-channel=msedge --headed
--slowmo - используется  для замедления выполнения теста на указанное количество миллисекунд.

pytest --slowmo 1000
--device - можно использовать для имитации поведения браузера для определенного устройства

В качества параметра передайте поддерживаемый девайс. Список поддерживаемых девайсов вы сможете  посмотреть по ссылке  
https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json

pytest --device="iPhone 13 Mini"


--output Каталог для артефактов, создаваемых тестами (по умолчанию: test-results).



--tracing Записывать ли трассировку для каждого теста. on, off или retain-on-failure (по умолчанию: off).



--video Записывать ли видео для каждого теста. on, off или retain-on-failure (по умолчанию: off).



--screenshot Должен ли автоматически делаться снимок экрана после каждого теста. on, off или only-on-failure (по умолчанию: off).

--full-page-screenshot - Следует ли делать скриншот всей страницы при ошибке. По умолчанию снимается только область просмотра. Требуется, чтобы параметр --screenshot был включен (по умолчанию: off).

как запустить Яндекс браузер 

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="chromium",executable_path="путь до яндекс браузера", headless=False)
        yield browser
        browser.close()

def test_yandex(browser):
    page = browser.new_page()
    page.goto("https://ya.ru/")


Дождаться загрузки

page.goto("https://playwright-todomvc.antonzimaiev.repl.co/#/", wait_until='domcontentloaded')

**Запись трассировки**
Чтобы записать трассировку, вам необходимо с помощью CLI  передать атрибут  --tracing и  выбрать вариант записи.

Доступные варианты записи трассировки:

'on'- Запишет трассировку для каждого теста. (не рекомендуется, так как производительность тяжелая)
'retain-on-failure'- Запишет трассировку для каждого теста, но удалит ее из успешных тестовых прогонов.
Команда для запуска всех тестов и сохранением трассировки только неудачных

pytest --tracing=retain-on-failure
После выполнения всех тестов должна появиться директория test-results с архивом trace.zip

 
Просмотр трассировки
Для просмотра выполните команду playwright show-trace и укажите адрес с записанному архиву трассировки

playwright show-trace trace.zip

