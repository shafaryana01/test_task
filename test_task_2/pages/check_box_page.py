from test_task_2.pages.base_page import BasePage
from test_task_2.pages.left_menu import LeftMenu


class CheckBoxPage(BasePage):
    CHECKBOX_SELECTION_LOCATOR = "//span[@class='rct-checkbox']"

    def __init__(self):
        self.left_menu = LeftMenu()
        super().__init__()

    def click_checkbox_selection(self):
        self.click(self.CHECKBOX_SELECTION_LOCATOR)
