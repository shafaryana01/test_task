from test_task_2.pages.base_page import BasePage


class LeftMenu(BasePage):
    CATEGORY_LOCATOR = "//*[.='{}']"

    def select_category(self, category_name):
        self.click(self.CATEGORY_LOCATOR.format(category_name))
