from time import sleep

import pytest

from test_appium.pages.base_page import BasePage
from test_appium.common_util import CommonUtil
from test_appium.pages.login_page import LoginPage
from test_appium.driver import driver
from test_appium.pages.optional_page import OptionalPage
from test_appium.pages.search_page import SearchPage
from test_appium.pages.xueqiu_page import XueqiuPage


class TestLogin:
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.commonutil = CommonUtil(self.driver)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("user, pwd, tips",[("999999999999999","123456","手机号"),("13169646888","123456","密码错误"),("13169646888","123456","太频繁")])
    def test_fail_login(self, user, pwd, tips):
        self.xueqiu.goto_login().goto_other_login()
        self.loginpage.login(user, pwd, tips)

        #清场的那个@用法。执行完之后回到首页
        self.loginpage.back_to_xueqiu()
        assert "基金" in self.driver.page_source


class TestSearch(BasePage):
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.search = SearchPage(self.driver)
    @pytest.mark.parametrize("key,name",[("alibaba","阿里巴巴"),("xiaomi","小米"),("google","谷歌")])
    def test_search(self,key,name):
        self.xueqiu.goto_search().search(key)
        assert name in self.driver.page_source
        self.search.find_by("id","action_close").click()


class TestOptional(BasePage):
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.search = SearchPage(self.driver)
        self.optional = OptionalPage(self.driver)

    def addoptional(self):
        self.xueqiu.goto_optional().goto_search().search("alibaba").addoptional()
        assert "已添加" in self.driver.page_source
        self.driver.keyevent(4)

    def test_addoptional(self):
        self.search.dropoptional()
        assert "加自选" in self.driver.page_source
        assert "已添加" not in self.driver.page_source
