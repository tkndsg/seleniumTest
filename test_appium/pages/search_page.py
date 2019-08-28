from test_appium.pages.base_page import BasePage


class SearchPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.keyevent(66)
        self.sleep(3)
        return self

    def addoptional(self):
        if self.is_element_exist("xpath", "//*[@text='BABA']/../../..//*[@text='加自选']"):
            self.driver.find_element_by_xpath("//*[@text='BABA']/../../..//*[@text='加自选']").click()
            if self.is_element_exist("xpath", "//*[@text='下次再说']"):
                self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        return self

    def dropoptional(self):
        if self.is_element_exist("xpath", "//*[@text='BABA']/../..//*[@text='已添加']"):
            print("需要点已添加")
            self.sleep(3)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("已添加");').click()
            print("已经点了已添加")
        return self