from time import sleep

import pytest
from appium import webdriver
from test_appium.pages.xueqiu_page import XueqiuPage


class TestLogin:
    def setup_class(self):
        self.xueqiu = XueqiuPage()

    def teardown_class(self):
        sleep(5)
        self.xueqiu.quit()

    @pytest.mark.parametrize("user, pwd, tips",
                             [("999999999999999", "123456", "手机号"),
                              ("13169646888", "123456", "密码错误"),
                              ("13169646888", "123456", "密码错误"),
                              ("13169646888","123456","太频繁")])
    def test_fail_login(self, user, pwd, tips):
        self.xueqiu.goto_login().goto_other_login().login(user, pwd, tips).back_to_xueqiu()
        assert "基金" in self.xueqiu.driver.page_source




