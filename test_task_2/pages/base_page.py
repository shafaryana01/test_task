from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _get_locator_by_type(self, locator):
        if locator.startswith("//") or locator.startswith(".//") or locator.startswith("("):
            return By.XPATH

        return By.CSS_SELECTOR

    def find_element(self, locator, time_out_sec=10):
        return self.wait_for_element_present(locator, time_out_sec)

    def wait_for_element_present(self, locator, time_out_sec=10):
        locator_by_type = self._get_locator_by_type(locator)

        element = WebDriverWait(self.driver, time_out_sec).until(
            EC.presence_of_element_located((locator_by_type, locator)))

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
        by_type = self._get_locator_by_type(locator)
        self.wait_for_element_present(locator)
        element = self.driver.find_element(by_type, locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_with_java_script(self, locator):
        by_type = self._get_locator_by_type(locator)
        self.wait_for_element_present(locator)
        element = self.driver.find_element(by_type, locator)
        self.driver.execute_script("arguments[0].click();", element)

