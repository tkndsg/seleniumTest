from appium import webdriver
from selenium.webdriver.common.by import By

from test_appium.pages.base_page import BasePage
from test_appium.pages.profile.login_page import LoginPage
from test_appium.pages.optional.optional_page import OptionalPage
from test_appium.pages.stock.search_page import SearchPage


class XueqiuPage(BasePage):
    driver = None
    appName = "com.xueqiu.android"
    appActivity = ".common.MainActivity"

    _edit_view_search = (By.ID, "tv_search")
    _image_view_login = (By.ID, "user_profile_icon")

    def __init__(self):
        if self.driver is None:
            self.first_start()
        else:
            self.driver.start_activity(self.appName, self.appActivity)

    def first_start(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Meizu16x"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

        XueqiuPage.driver = self.driver

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




