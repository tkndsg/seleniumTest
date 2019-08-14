from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_po.base_page import BasePage


class MaterialBase(BasePage):
    _text_tabnav = (By.CSS_SELECTOR, ".ww_icon_GrayText")
    _picture_tabnav = (By.CSS_SELECTOR, ".ww_icon_GrayPic")
    _upload_img_btn = (By.CSS_SELECTOR, ".js_upload_file_selector")
    _upload_img = (By.XPATH, '//*[@id="js_upload_input"]')
    _upload_img_loading_cancer = (By.XPATH, '//*[@text="取消"]')
    _upload_img_dialog_next_btn = (By.CSS_SELECTOR, ".ww_diaglog_foot_cnt .js_next")

    def change_lib(self, libname):
        if libname == "文字":
            locator = self._text_tabnav
        elif libname == "图片":
            locator = self._picture_tabnav
        else :
            locator = "图片"
        self.driver.find_element(*locator).click()

    def goto_materialbase(self, addmaterial):
        pass

    def upload_picture(self, relativepath):
        realpath = self.change_to_absolute_path(relativepath)
        self.driver.find_element(*self._upload_img_btn).click()
        img_upload_btn = self.driver.find_element(*self._upload_img)
        img_upload_btn.send_keys(realpath)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.invisibility_of_element_located(self._upload_img_loading_cancer))
        self.driver.find_element(*self._upload_img_dialog_next_btn).click()

