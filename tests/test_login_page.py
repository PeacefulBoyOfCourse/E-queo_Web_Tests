from pages.login_page import LoginPage
from pages.base_page import BasePage


class TestCompanyLoginPage:
    def test_guest_can_enter_company_login_page(self, browser):
        url = "https://test.test-eq.ru"
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.should_be_login_url()

    def test_guest_can_log_in_by_credits(self, browser, log_in_user_by_credits):
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()
