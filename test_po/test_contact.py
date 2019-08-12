from time import sleep

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from test_po.base_page import BasePage
from test_po.contact_page import ContactPage
from test_po.profile_page import ProfilePage
from test_po.wework_page import WeworkPage


class TestContact:
    def setup_class(self):
        self.wework = WeworkPage()
        self.contact = ContactPage(self.wework.driver)
        self.wework.driver.implicitly_wait(5)

    def teardown_class(self):
        sleep(2)
        self.wework.quit()

    def test_addmember(self):
        self.contact.add_member("tkn1", "tkn1", "13100000000", 0)

    def test_search(self):
        self.contact.search("林")
        pass

    def test_deletemember(self):
        pass

