from test_task_2.pages.base_page import BasePage


class RadioButtonPage(BasePage):
    IMPRESSIVE_LOCATOR = "//input[@id='impressiveRadio']"
    YES_LOCATOR = "//input[@id='yesRadio']"

    def choose_impressive(self):
        self.click_with_java_script(self.IMPRESSIVE_LOCATOR)

    def choose_yes(self):
        self.click_with_java_script(self.YES_LOCATOR)
