from time import sleep
from selenium.webdriver.common.by import By
from test_po.base_page import BasePage
from test_po.profile_page import ProfilePage


class ContactPage(BasePage):
    _contact_tab =(By.XPATH, '//*[@id="menu_contacts"]/span')
    _add_member_but = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")     # 添加成员
    _upload_picture_icon = (By.XPATH, '//*[@id="js_upload_file"]/div/div[2]')
    _choose_img_btn = (By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input')
    _ssm_check = (By.CSS_SELECTOR, ".ww_label_Middle .ww_checkbox")
    _comfire_save_btn = (By.CSS_SELECTOR, ".js_btn_save")
    _commit_img_btn = (By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[3]/a[1]')
    _name_input = (By.XPATH, '//*[@id="username"]')
    _username_input= (By.XPATH, '//*[@id="memberAdd_acctid"]')
    _phone_input = (By.XPATH, '//*[@id="memberAdd_phone"]')
    _search_input = (By.ID, 'memberSearchInput')

    def come_to_contact_tab(self):
        self.driver.find_element(*self._contact_tab).click()

    def add_member(self,name, username, phone, ssm,**kwargs):
        self.come_to_contact_tab()
        # 进入新增页面
        sleep(2)
        self.driver.find_element(*self._add_member_but).click()

        # 上传头像
        self.upload_img("/images/cat.jpg")

        # 填写信息
        self.driver.find_element(*self._name_input).send_keys(name)
        self.driver.find_element(*self._username_input).send_keys(username)
        self.driver.find_element(*self._phone_input).send_keys(phone)

        # 下滑页面
        self.slip_down("250")

        # 点击发送短信按钮
        if ssm == 0:
            self.driver.find_element(*self._ssm_check).click()

        # 点保存按钮
        self.driver.find_element(*self._comfire_save_btn).click()
        return self

    def delete_member(self):
        pass

    def search(self, key):
        self.come_to_contact_tab()
        search_input = self.driver.find_element(*self._search_input)
        search_input.clear()
        search_input.send_keys(key)
        return ProfilePage(self.driver)

    def get_tips(self):
        return "OK"

    def upload_img(self, img_relative_path):
        upload_picture_icon = self.driver.find_element(*self._upload_picture_icon)
        self.driver.execute_script("arguments[0].click()", upload_picture_icon)
        real_path = self.change_to_absolute_path(img_relative_path)
        choose_img_btn = self.driver.find_element(*self._choose_img_btn)
        choose_img_btn.send_keys(real_path)
        self.driver.find_element(*self._commit_img_btn).click()




