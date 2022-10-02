from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert 'login' in self.browser.current_url
