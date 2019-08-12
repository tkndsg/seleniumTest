import time
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    _add_member_but = ("link_text", "添加成员")     # 添加成员

    def add_member(self,name, username, phone, ssm,**kwargs):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
        # 上传头像
        upload_img_btn = self.driver.find_element(By.XPATH, '//*[@id="js_upload_file"]/div/div[2]')
        # todo change to a function
        self.driver.execute_script("arguments[0].click()", upload_img_btn)
        uploading = self.driver.find_element(By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input')
        img_path = self.change_to_absolute_path("/images/cat.jpg")
        uploading.send_keys(img_path)
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[3]/a[1]').click()

        # 填写信息
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)

        # 下滑页面，点保存按钮
        self.driver.execute_script("window.scrollBy(0,300)")
        if ssm == 0:
            self.driver.find_element(By.CSS_SELECTOR, ".ww_label_Middle .ww_checkbox").click()
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return self

    def delete_member(self):
        pass

    def search(self, key):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        self.driver.find_element(By.ID, 'memberSearchInput').send_keys(key)
        return ProfilePage(self.driver)

    def get_tips(self):
        return "OK"


