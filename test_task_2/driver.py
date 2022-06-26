from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Driver:
    _driver = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Driver, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        if Driver._driver is None:
            Driver._driver = self.create_driver()

    @staticmethod
    def create_driver():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        return driver

    @classmethod
    def get_driver(cls):
        return Driver._driver

    @classmethod
    def quit(cls):
        Driver._driver.quit()
        Driver._driver = None
