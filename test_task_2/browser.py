from test_task_2.driver import Driver


class Browser:

    def __init__(self):
        self.driver = Driver().get_driver()

    def open_url(self, url):
        self.driver.get(url)
