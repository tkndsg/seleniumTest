from test_appium.base_page import BasePage
from test_appium.login_page import LoginPage
from test_appium.search_page import SearchPage


class XueqiuPage(BasePage):
    def go_tosearch(self):
        self.driver.find_element_by_id("tv_search").click()
        return SearchPage(self.driver)

    def gotologin(self):
        self.driver.find_element_by_xpath("//*[@text='雪球']").click()
        return LoginPage(self.driver)


