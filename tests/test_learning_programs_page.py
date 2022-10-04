from pages.base_page import BasePage


class TestLearningProgramsPage:
    def test_open_learning_programs_page(self, browser, log_in_user_by_credits):
        base_page = BasePage(browser, browser.current_url)
        base_page.should_open_lp_page()
