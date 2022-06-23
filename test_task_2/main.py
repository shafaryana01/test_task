import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from test_task_2.pages.check_box_page import CheckBoxPage
from test_task_2.pages.left_menu import LeftMenu
from test_task_2.pages.main_page import MainPage
from test_task_2.pages.radio_button_page import RadioButtonPage

driver = webdriver.Chrome(ChromeDriverManager().install())

main_page = MainPage(driver)
left_menu = LeftMenu(driver)
check_box_page = CheckBoxPage(driver)
radio_button_page = RadioButtonPage(driver)

main_page.navigate()
driver.maximize_window()
main_page.scroll_to_element()
time.sleep(1)
main_page.select_category()
time.sleep(1)
left_menu.select_check_box()
time.sleep(1)
check_box_page.click_checkbox_selection()
time.sleep(1)
left_menu.select_radio_button()
time.sleep(1)
radio_button_page.choose_impressive()
time.sleep(1)
radio_button_page.choose_yes()


time.sleep(5)
