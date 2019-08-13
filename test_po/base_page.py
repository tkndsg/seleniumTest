import os
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_by_js(self, by, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((by,locator)))
        sleep(3)
        self.driver.execute_script("arguments[0].click;", self.driver.find_element(by,locator))

    def change_to_absolute_path(self,relative_path):
        absolute_path = (os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+relative_path).replace("/", "\\")
        return absolute_path

    def slip_down(self, step=300):
        scrip_content = "window.scrollBy(0,"+step+")"
        self.driver.execute_script(scrip_content)
