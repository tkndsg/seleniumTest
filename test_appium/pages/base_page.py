import logging
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def sleep(self, param):
        time.sleep(param)

    def quit(self):
        self.driver.quit()

    def find_by(self, *loc):
        return self.driver.find_element(*loc)

    def wait_element_appear(self, *loc):
        try:
            return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(*loc))
        except Exception:
            logging.info(Exception)
            return None

    def is_element_exist(self, *loc):
        flag = None
        self.sleep(1)
        try:
            self.driver.find_element(*loc)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag

    def click_if_element_exit(self, *loc):
        self.sleep(1)
        try:
            self.driver.find_element(*loc).click()
        except NoSuchElementException :
            print(*loc)
            logging.info(Exception)
            logging.info("没有找到，所以没有点击")
