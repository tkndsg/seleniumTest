from test_appium.base_page import BasePage


class LoginPage(BasePage):
    def goto_other_login(self):
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'user_profile_icon')]").click()
        self.driver.find_element_by_xpath("//*[contains(@resource-id,'login_more')]").click()

    def login(self,phone,password):
        self.driver.find_element_by_id("login_account").send_keys("9999999999999999")
        self.driver.find_element_by_id("login_password").send_keys("123456")
        self.driver.find_element_by_id("button_next").click()

