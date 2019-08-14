from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_po.base_page import BasePage
from test_po.contact_page import ContactPage
from test_po.managetool_page import ManageTool_Page
from test_po.materialbase_page import MaterialBase
from test_po.profile_page import ProfilePage
from test_po.wework_page import WeworkPage


class TestManageTool:
    def setup_class(self):
        self.wework = WeworkPage()
        self.managetoolpage = ManageTool_Page(self.wework.driver)
        self.materialbasepage = MaterialBase(self.wework.driver)
        self.wework.driver.implicitly_wait(5)

    def teardown_class(self):
        sleep(5)
        self.wework.quit()

    def test_goto_materilbase(self):
        self.managetoolpage.goto_tab("管理工具")
        self.managetoolpage.goto_materialbase()
        self.materialbasepage.change_lib("图片")
        self.materialbasepage.upload_picture("/images/cat1.jpg")
