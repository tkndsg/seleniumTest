import time

from selenium.webdriver.remote.webdriver import WebDriver

from test_po.common_util import CommonUtil


class BasePage:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def sleep(self, param):
        time.sleep(param)

    def find_by(self, by, locator):
        return self.driver.find_element(by, locator)
