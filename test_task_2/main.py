from test_task_2 import config
from test_task_2.browser import Browser
from test_task_2.driver import Driver
from test_task_2.pages.check_box_page import CheckBoxPage
from test_task_2.pages.main_page import MainPage
from test_task_2.pages.radio_button_page import RadioButtonPage


class Task2:
    main_page = MainPage()
    check_box_page = CheckBoxPage()
    radio_button_page = RadioButtonPage()

    def task_2(self):
        self.main_page.scroll_to_element()
        self.main_page.select_category()
        self.check_box_page.left_menu.select_category(config.CHECK_BOX)
        self.check_box_page.click_checkbox_selection()
        self.radio_button_page.left_menu.select_category(config.RADIO_BUTTON)
        self.radio_button_page.choose_button(config.IMPRESSIVE_ID)
        self.radio_button_page.choose_button(config.YES_ID)


if __name__ == "__main__":
    Browser().open_url(config.URL)
    Task2().task_2()
    Driver.quit()
