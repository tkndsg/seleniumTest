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

    @pytest.mark.parametrize("user, pwd, tips",
                             [("999999999999999", "123456", "手机号"),
                              ("13169646888", "123456", "密码错误"),
                              ("13169646888", "123456", "密码错误"),
                              ("13169646888","123456","太频繁")])
    def test_fail_login(self, user, pwd, tips):
        self.xueqiu.goto_login().goto_other_login()
        self.loginpage.login(user, pwd, tips)
        self.loginpage.back_to_xueqiu()
        assert "基金" in self.driver.page_source


class TestSearch:
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.search = SearchPage(self.driver)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("key, name", [("alibaba", "阿里巴巴"), ("xiaomi", "小米"), ("google", "谷歌")])
    def test_search(self,key,name):
        self.xueqiu.goto_search().search(key)
        assert name in self.driver.page_source
        self.search.back_to_xuqiu()


class TestOptional:
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.search = SearchPage(self.driver)
        self.optional = OptionalPage(self.driver)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("keyword, stock_name, symbol",[("alibaba", "阿里巴巴", "BABA"), ])
    def test_addoptional(self, keyword, stock_name, symbol):
        self.xueqiu.goto_optional().goto_search().search(keyword).addoptional(symbol).back_to_xuqiu()
        assert stock_name, symbol in self.driver.page_source
        self.driver.keyevent(4)

    def test_dropoptional(self):
        self.xueqiu.goto_optional().dropoptional()
        assert "加自选" in self.driver.page_source
        assert "已添加" not in self.driver.page_source

    # todo 两个地方的删除自选功能
    # 分别在自选页面和在搜索结果页面都可以加一个~
