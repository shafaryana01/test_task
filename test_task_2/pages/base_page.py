from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_task_2.driver import Driver


class BasePage:
    def __init__(self):
        self.driver = Driver().get_driver()
        self.locator_type = By.XPATH

    def find_element(self, locator, time_out_sec=10):
        return self.wait_for_element_present(locator, time_out_sec)

    def wait_for_element_present(self, locator, time_out_sec=10):

        element = WebDriverWait(self.driver, time_out_sec).until(
            EC.presence_of_element_located((self.locator_type, locator)))

        return element

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def open_url(self, url):
        self.driver.get(url)

    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def scroll_to_element_view(self, locator):
        self.wait_for_element_present(locator)
        element = self.driver.find_element(self.locator_type, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_with_java_script(self, locator):
        self.wait_for_element_present(locator)
        element = self.driver.find_element(self.locator_type, locator)
        self.driver.execute_script("arguments[0].click();", element)
