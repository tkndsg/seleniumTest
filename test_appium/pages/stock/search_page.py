from appium.webdriver.common.touch_action import TouchAction

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
        print("//*[@text='%s']/../..//*[@text='已添加']" % symbol)
        self.driver.find_element("xpath", "//*[@text='%s']/../../..//*[@text='已添加']" % symbol).click()
        return self

    def dropoptional_longpress(self, symbol):
        # todo 这块没有做

        e1 = self.driver.find_element("xpath", "//*[@text='%s']/../../..//*[@text='加自选']" % symbol)
        TouchAction.long_press(e1)

        # todo 这块需要做
        print("//*[@text='%s']/../..//*[@text='已添加']" % symbol)
        self.driver.find_element("xpath", "//*[@text='%s']/../../..//*[@text='已添加']" % symbol).click()
        return self

    def back_to_xuqiu(self):
        self.find_by("id", "action_close").click()