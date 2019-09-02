from test_appium.pages.base_page import BasePage


class SearchPage(BasePage):
    _next_time = ("xpath", "//*[@text='下次再说']")

    def search(self, keyword):
        print("开始search开始搜索")
        self.driver.find_element("id", "search_input_text").send_keys(keyword)
        self.driver.keyevent(66)
        self.sleep(3)
        return self

    def addoptional(self, symbol):
        self.driver.find_element("xpath", "//*[@text='%s']/../../..//*[@text='加自选']" % symbol).click()
        self.click_if_element_exit(*self._next_time)
        return self

    def dropoptional(self, symbol):
        self.driver.find_element("xpath", "//*[@text='%s']/../..//*[@text='已添加']" % symbol).click()
            # self.driver.find_element_by_android_uiautomator('new UiSelector().text("已添加");').click()
        return self

    def back_to_xuqiu(self):
        self.find_by("id", "action_close").click()