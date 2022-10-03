from pages.login_page import LoginPage


class TestCompanyLoginPage:
    def test_guest_can_enter_company_login_page(self, browser):
        url = "https://test.test-eq.ru"
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.should_be_login_url()

    def test_guest_can_log_in_by_credits(self, browser):
        url = "https://test.test-eq.ru"
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.click_log_in_by_credits_button()
        login_page.enter_credits()
        login_page.click_log_in_button()
        login_page.should_be_authorized_user()
