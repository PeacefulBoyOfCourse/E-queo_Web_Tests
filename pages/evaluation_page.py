from pages.base_page import BasePage
from .locators import EvaluationPageLocators, BasePageLocators


class EvaluationPage(BasePage):
    def should_open_evaluation_page(self):
        self.click_side_menu_evaluation_icon()
        assert self.browser.find_element(*EvaluationPageLocators.EVALUATION_PAGE_H1_HEADER), "Evaluation page is not " \
                                                                                             "available. "

