from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_po.base_page import BasePage


class ProfilePage(BasePage):
    _edit_btn = (By.CSS_SELECTOR, '.ww_operationBar .js_edit')
    _disable_btn = (By.CSS_SELECTOR, ".ww_operationBar .js_disable")
    _name_input = (By.XPATH, '//*[@id="username"]')
    _phone_input = (By.XPATH, '//*[@id="memberEdit_phone"]')
    _comfire_save_btn = (By.CSS_SELECTOR, ".js_save")
    _dialog_submit_btn = (By.CSS_SELECTOR, ".ww_dialog_foot .ww_btn_Blue")

    def update(self, key, newvalue):
        self.driver.find_element(*self._edit_btn).click()
        if key == "name":
            item = self.driver.find_element(*self._name_input)
            item.clear()
            item.send_keys(newvalue)
        elif key == "phone":
            item = self.driver.find_element(*self._phone_input)
            item.clear()
            item.send_keys(newvalue)
        self.driver.find_element(*self._comfire_save_btn).click()
        return self

    def enable(self,flag):
        self.sleep(2)
        self.driver.find_element(*self._disable_btn).click()
        if flag == 0:
           self.driver.find_element(*self._dialog_submit_btn).click()
        return self

    def delete(self):
        pass

    def invite(self):
        pass
