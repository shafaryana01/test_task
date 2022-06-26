from test_task_2.pages.base_page import BasePage
from test_task_2.pages.left_menu import LeftMenu


class RadioButtonPage(BasePage):
    RADIO_BUTTON_LOCATOR = "//input[@id='{}']"

    def __init__(self):
        self.left_menu = LeftMenu()
        super().__init__()

    def choose_button(self, name):
        self.click_with_java_script(self.RADIO_BUTTON_LOCATOR.format(name))
