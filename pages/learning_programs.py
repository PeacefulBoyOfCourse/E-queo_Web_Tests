from pages.base_page import BasePage
from pages.locators import LearningProgramsPageLocators


class LearningPrograms(BasePage):
    def should_open_lp_page(self):
        self.click_side_menu_lp_icon()
        assert self.browser.find_element(*LearningProgramsPageLocators.LP_PAGE_H1_HEADER), "Learning programs page " \
                                                                                           "is not available."
