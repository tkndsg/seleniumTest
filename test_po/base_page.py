import os
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _index_tab = (By.XPATH, '//*[@id="menu_index"]/span')
    _contact_tab = (By.XPATH, '//*[@id="menu_contacts"]/span')
    _managetool_tab = (By.XPATH, '//*[@id="menu_manageTools"]/span')

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

    def sleep(self,second):
        sleep(second)

    def goto_tab(self, tabname):
        if tabname == "首页":
            self.driver.find_element(*self._index_tab).click()
        if tabname == "通讯录":
            self.driver.find_element(*self._contact_tab).click()
        if tabname == "管理工具":
            self.driver.find_element(*self._managetool_tab).click()
