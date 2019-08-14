from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from test_po.base_page import BasePage


class ManageTool_Page(BasePage):
    _materialbase_item = (By.XPATH, "//*[text()='素材库']")
    def goto_menberadd(self):
        pass

    def goto_materialbase(self):
        self.driver.find_element(*self._materialbase_item).click()

