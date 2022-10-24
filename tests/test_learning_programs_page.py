from pages.learning_programs import LearningPrograms


class TestLearningProgramsPage:
    def test_open_learning_programs_page(self, browser, log_in_user_by_credits):
        lp_page = LearningPrograms(browser, browser.current_url)
        lp_page.should_open_lp_page()
