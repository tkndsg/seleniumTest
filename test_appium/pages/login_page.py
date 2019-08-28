from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.base_page import BasePage


class LoginPage(BasePage):
    _edit_account = ("id", "login_account")
    _edit_password = ("id", "login_password")
    _btn_login = ("id", "button_next")
    _btn_ok = ("xpath", "//*[@text='确定']")

    def goto_other_login(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'login_more')]").click()

    def login(self,phone, password, tips):
        locator = "//*[@text='"+tips+"']"
        print(locator)
        self.driver.find_element(*self._edit_account).send_keys(phone)
        self.driver.find_element(*self._edit_password).send_keys(password)
        self.driver.find_element(*self._btn_login).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element("xpath", locator))
        self.driver.find_element(*self._btn_ok).click()

    def back_to_xueqiu(self):
        self.driver.find_element_by_id("iv_action_back").click()
        self.driver.find_element_by_id("md_buttonDefaultNegative").click()
        self.driver.keyevent(4)
