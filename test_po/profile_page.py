from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_po.base_page import BasePage


class ProfilePage(BasePage):
    def update(self, key, newvalue):
        self.click_by_js(By.CSS_SELECTOR, '.ww_operationBar .js_edit')
        pass

    def disable(self):
        pass

    def delete(self):
        pass

    def invite(self):
        pass
