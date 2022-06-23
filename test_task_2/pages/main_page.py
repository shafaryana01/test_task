from test_task_2.pages.base_page import BasePage


class MainPage(BasePage):

    CATEGORY_LOCATOR = "//*[.='{}']"

    URL = "https://demoqa.com/"

    def navigate(self):
        self.open_url(self.URL)

    def scroll_to_element(self, category="Alerts, Frame & Windows"):
        self.scroll_to_element_view(self.CATEGORY_LOCATOR.format(category))

    def select_category(self, category="Elements"):
        self.click(self.CATEGORY_LOCATOR.format(category))
