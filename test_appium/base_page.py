import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver

from test_po.common_util import CommonUtil


class BasePage:
    def __init__(self,driver: WebDriver):
        self.driver = driver

    def sleep(self, param):
        time.sleep(param)

    def find_by(self, by, locator):
        return self.driver.find_element(by, locator)

    def is_element_exist(self, by, locator):
        flag = None
        self.sleep(1)
        try:
            self.driver.find_element(by,locator)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag
