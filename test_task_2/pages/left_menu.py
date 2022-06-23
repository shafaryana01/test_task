from test_task_2.pages.base_page import BasePage


class LeftMenu(BasePage):
    CHECK_BOX_LOCATOR = "//*[.='Check Box']"
    RADIO_BUTTON_LOCATOR = "//*[.='Radio Button']"

    def select_check_box(self):
        self.click(self.CHECK_BOX_LOCATOR)

    def select_radio_button(self):
        self.click(self.RADIO_BUTTON_LOCATOR)
