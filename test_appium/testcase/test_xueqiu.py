import os
from time import sleep

import pytest
from appium import webdriver
from test_appium.pages.profile.login_page import LoginPage
from test_appium.pages.optional.optional_page import OptionalPage
from test_appium.pages.stock.search_page import SearchPage
from test_appium.pages.xueqiu_page import XueqiuPage


class TestLogin:
    def setup_class(self):
        self.xueqiu = XueqiuPage()

    def test_initialization(self):
        os.popen("adb shell pm clear com.xueqiu.android")

    def teardown_class(self):
        sleep(5)
        self.xueqiu.quit()


