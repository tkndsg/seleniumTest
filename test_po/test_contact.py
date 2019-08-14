from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_po.base_page import BasePage
from test_po.contact_page import ContactPage
from test_po.profile_page import ProfilePage
from test_po.wework_page import WeworkPage


class TestContact:
    def setup_class(self):
        self.wework = WeworkPage()
        self.contact = ContactPage(self.wework.driver)
        self.profile = ProfilePage(self.wework.driver)
        self.wework.driver.implicitly_wait(5)

    def teardown_class(self):
        sleep(5)
        self.wework.quit()

    def test_addmember(self):
        self.contact.add_member("小老弟", "xld", "13100000000", 0)

    def test_update(self):
        self.contact.search("林").update("phone", "13100000001")

    def test_enable(self):
        self.contact.search("小").enable(0).enable(1)
        assert "邀请加入" in self.wework.driver.page_source

    def test_deletemember(self):
        pass
