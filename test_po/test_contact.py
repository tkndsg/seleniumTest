from time import sleep

from selenium import webdriver
import pytest

from test_po.contact_page import ContactPage
from test_po.wework_page import WeworkPage


class TestContact:
    def setup_class(self):
        self.wework = WeworkPage()
        self.contact = ContactPage(self.wework)

    def teardown_class(self):
        sleep(5)
        self.wework.quit()

    def test_addmember(self):
        self.contact.add_member("tkn1", "tkn1", "13100000000", 0)

    def test_deletemember(self):
        pass
