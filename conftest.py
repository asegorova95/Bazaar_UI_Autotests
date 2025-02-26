import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# Добавляем аргументы командной строки для pytest
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Выбор браузера: chrome, firefox")
    parser.addoption("--headless", action="store_true", help="Запуск в headless режиме (без UI)")
    parser.addoption("--window_size", action="store", default="max", help="Размер окна: max или ширина,высота")

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    window_size = request.config.getoption("--window_size")

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Браузер {browser} не поддерживается!")

    driver.get("https://dev.bazaarorigin.com/")# Настройка размера окна
    if window_size == "max":
        driver.maximize_window()
    else:
        width, height = map(int, window_size.split(","))
        driver.set_window_size(width, height)

    request.cls.driver = driver
    yield driver
    driver.quit()
