from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverFactory:

    @staticmethod
    def create_driver():
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=options)
        return driver
