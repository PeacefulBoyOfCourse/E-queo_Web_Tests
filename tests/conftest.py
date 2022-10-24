from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

from pages.login_page import LoginPage


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Choose browser language: ru, en')


@pytest.fixture(scope="class")
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


@pytest.fixture(scope="class")
def log_in_user_by_credits(browser):
    url = "https://test.test-eq.ru"
    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.click_log_in_by_credits_button()
    login_page.enter_credits()
    login_page.click_log_in_button()

