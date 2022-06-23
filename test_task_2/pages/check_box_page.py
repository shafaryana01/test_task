from test_task_2.pages.base_page import BasePage


class CheckBoxPage(BasePage):
    CHECKBOX_SELECTION_LOCATOR = "//span[@class='rct-checkbox']"

    def click_checkbox_selection(self):
        self.click(self.CHECKBOX_SELECTION_LOCATOR)


