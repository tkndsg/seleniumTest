from test_appium.base_page import BasePage
from test_appium.search_page import SearchPage


class OptionalPage(BasePage):
    def gotosearch(self):
        self.driver.find_element_by_xpath("//*[@text='雪球']").click()
        return SearchPage(self.driver)

    def addoptional(self):
        return self

    def dropoptional(self):
        return self
