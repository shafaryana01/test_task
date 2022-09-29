from test_task_2.pages.base_page import BasePage


class MainPage(BasePage):

    CATEGORY_LOCATOR = "//*[.='Elements']"

    def scroll_to_element(self):
        self.scroll_to_element_view(self.CATEGORY_LOCATOR)

    def select_category(self):
        self.click(self.CATEGORY_LOCATOR)
