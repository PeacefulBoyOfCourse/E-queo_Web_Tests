from pages.evaluation_page import EvaluationPage


class TestEvaluationPage:
    def test_open_evaluation_page(self, browser, log_in_user_by_credits):
        evaluation_page = EvaluationPage(browser, browser.current_url)
        evaluation_page.should_open_evaluation_page()
