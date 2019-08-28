from selenium.webdriver.common.by import By

from test_appium.pages.base_page import BasePage
from test_appium.pages.login_page import LoginPage
from test_appium.pages.optional_page import OptionalPage
from test_appium.pages.search_page import SearchPage


class XueqiuPage(BasePage):
    _edit_view_search = (By.ID, "tv_search")
    _image_view_login = (By.ID, "user_profile_icon")

    def goto_search(self):
        self.driver.find_element(*self._edit_view_search).click()
        return SearchPage(self.driver)

    def goto_login(self):
        self.driver.find_element(*self._image_view_login).click()
        return LoginPage(self.driver)

    def goto_optional(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("自选");').click()
        if self.is_element_exist("xpath", "//*[@text='新增手势切换、指标设置功能']"):
            self.driver.keyevent(4)
        return OptionalPage(self.driver)


