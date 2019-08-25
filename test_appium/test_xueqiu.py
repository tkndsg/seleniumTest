from time import sleep

import pytest

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from test_appium.base_page import BasePage
from test_appium.common_util import CommonUtil
from test_appium.login_page import LoginPage
from test_appium.driver import driver
from test_appium.search_page import SearchPage
from test_appium.xueqiu_page import XueqiuPage


class TestLogin(BasePage):
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.commonutil = CommonUtil(self.driver)
        self.search = SearchPage(self.driver)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    def test_wrong_phone(self):
        self.loginpage.goto_other_login()

        self.loginpage.login("999999999999999","123456")

        self.loginpage.find_by("id","button_next").click()

        assert "手机号码填写错误" in self.driver.page_source

        self.loginpage.find_by("XPATH","//*[@text='确定']").click()

    def test_wrong_password(self):
        self.loginpage.login("13169646888","123456")
        self.loginpage.find_by("id","button_next").click()

        if self.commonutil.isElementExist("xpath", "//*[@text='请求太频繁，请稍后再试']"):
            pass
        else:
            assert "用户名或密码错误" in self.driver.page_source
        self.driver.find_element_by_xpath("//*[@text='确定']").click()

        self.driver.find_element_by_id("iv_action_back").click()
        self.driver.find_element_by_id("md_buttonDefaultNegative").click()
        self.driver.keyevent(4)

        assert "基金" in self.driver.page_source

    @pytest.mark.parametrize("key,name",[("alibaba","阿里巴巴"),("xiaomi","小米"),("google","谷歌")])
    def test_search(self,key,name):
        self.xueqiu.go_tosearch().search(key)
        assert name in self.driver.page_source
        self.search.find_by("id","action_close").click()

    def addoptional(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("自选");').click()
        if self.commonutil.isElementExist("xpath", "//*[@text='新增手势切换、指标设置功能']"):
            self.driver.keyevent(4)
        self.driver.find_element_by_id("action_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        self.driver.keyevent(66)
        if self.commonutil.isElementExist("xpath", "//*[@text='BABA']/../../..//*[@text='加自选']"):
            self.driver.find_element_by_xpath("//*[@text='BABA']/../../..//*[@text='加自选']").click()
            if self.commonutil.isElementExist("xpath", "//*[@text='下次再说']"):
                self.driver.find_element_by_xpath("//*[@text='下次再说']").click()

        elif self.commonutil.isElementExist("xpath", "//*[@text='BABA']/../..//*[@text='已添加']"):
            print("需要点已添加")
            sleep(3)
            self.driver.find_element_by_android_uiautomator('new UiSelector().text("已添加");').click()
            print("已经点了已添加")

    def test_addoptional(self):
        self.addoptional()
        assert "已添加" in self.driver.page_source
        self.driver.keyevent(4)
        self.addoptional()
        assert "加自选" in self.driver.page_source
        assert "已添加" not in self.driver.page_source


