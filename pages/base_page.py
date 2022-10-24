from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import requests
from .locators import *


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def open(self):
        r = requests.get(self.url)
        assert r.status_code == 200, "Response code is not 200"
        self.browser.get(self.url)

    def click_side_menu_evaluation_icon(self):
        evaluation_button = self.browser.find_element(*BasePageLocators.EVALUATION_PAGE_BUTTON)
        evaluation_button.click()

    def click_side_menu_lp_icon(self):
        lp_button = self.browser.find_element(*BasePageLocators.LP_PAGE_BUTTON)
        lp_button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.PROFILE_HEAD_INFO), "User is not authorised"
