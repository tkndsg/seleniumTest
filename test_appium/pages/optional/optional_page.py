from appium.webdriver.common.touch_action import TouchAction

from test_appium.pages.base_page import BasePage
from test_appium.pages.stock.search_page import SearchPage


class OptionalPage(BasePage):
    def goto_search(self):
        print("点击搜索框goto_search")
        self.driver.find_element("id", "action_search").click()
        return SearchPage(self.driver)

    def addoptional(self):
        if self.is_element_exist("xpath", "//*[@text='BABA']/../../..//*[@text='加自选']"):
            self.driver.find_element_by_xpath("//*[@text='BABA']/../../..//*[@text='加自选']").click()
            if self.is_element_exist("xpath", "//*[@text='下次再说']"):
                self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        return self

    def dropoptional(self, symbol):
        stock = self.driver.find_element("xpath", "//*[@text='%s']" % symbol)
        print("//*@text='%s']" % symbol)
        TouchAction(self.driver).long_press(stock).perform()
        self.driver.find_element("xpath", "//*[@text='删除']")
        return self
