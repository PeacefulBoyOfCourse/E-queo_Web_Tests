from pages.base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def click_log_in_by_credits_button(self):
        log_in_by_credits_button = self.browser.find_element(*LoginPageLocators.LOG_IN_BY_CREDITS_BUTTON)
        log_in_by_credits_button.click()

    def enter_credits(self):
        self.enter_login()
        self.enter_password()

    def enter_login(self):
        login_field = self.browser.find_element(*LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys('egtestuser')

    def enter_password(self):
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys('qwerty123')

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def click_log_in_button(self):
        log_in_button = self.browser.find_element(*LoginPageLocators.LOG_IN_BUTTON)
        log_in_button.click()
