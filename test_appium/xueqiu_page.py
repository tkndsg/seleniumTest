from test_appium.base_page import BasePage
from test_appium.login_page import LoginPage
from test_appium.optional_page import OptionalPage
from test_appium.search_page import SearchPage


class XueqiuPage(BasePage):
    def goto_search(self):
        self.driver.find_element_by_id("tv_search").click()
        return SearchPage(self.driver)

    def goto_login(self):
        self.driver.find_element_by_xpath("//*[@text='雪球']").click()
        return LoginPage(self.driver)

    def goto_optional(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("自选");').click()
        if self.is_element_exist("xpath", "//*[@text='新增手势切换、指标设置功能']"):
            self.driver.keyevent(4)
        return OptionalPage(self.driver)


