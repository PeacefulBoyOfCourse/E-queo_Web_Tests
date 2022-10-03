from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose browser language: ru, en')


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")

    print("\nstart chrome browser for test..")
    options = Options()
    # options.add_argument('headless')  # activate to use non-UI
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1366, 768)
    yield browser
    print("\nquit browser..")
    browser.quit()
