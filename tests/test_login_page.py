from pages.login_page import LoginPage


class TestLoginPage:
    def test_guest_can_log_in(self, browser):
        url = "https://test.test-eq.ru"
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.should_be_login_url()
