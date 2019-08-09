from time import sleep

from selenium import webdriver
import pytest

from test_po.contact_page import ContactPage


class TestContact:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        cookies = {
            "wwrtx.i18n_lan_key":"zh-CN%2Czh%3Bq%3D0.9",
            "wwrtx.i18n_lan":"zh-cn",
            "wwrtx.ref":"direct",
            "wwrtx.refid":"5198630543019914",
            "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d":"1565247025",
            "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d":"1565247025",
            "_ga":"GA1.2.199702808.1565247025",
            "_gid":"GA1.2.416749027.1565247025",
            "_gat":"1",
            "wwrtx.d2st":"a9486608",
            "wwrtx.sid":"ZRNJMZN4hWEA-UnHCIGv0-q2Q3s_vPy4i8msNNU9Ttkj5hL_GCnDcrDVqhaSBf44",
            "wwrtx.ltype":"1",
            "wxpay.corpid":"1970324979080668",
            "wxpay.vid":"1688851045936785",
            "wwrtx.vst":"p5k-r-w2kxcOOuYPi_iKg2blsShUOlKiTjy5zmiEgAeAVvq1GlHzMaH6UOUMOMCHVqJPJdYpU7KxLNcMLWXIPBb9UNSOrwb474EtNW5zhNR3Si7vepQ_OLZ3ZeFAQ3VakvCAkoA0GK8gHdrV1PEFPDzMwOfp1e75TyDNZg-a3LZReVWL_X3v77mVhWGAsy6CB9BYLGcK0lY-aO2WyyCbFBhRSuPY5VbS5fX17-q5i0K3aOIN_V1H_3QrG2C0eH4E8p2lqF2G5Lpo_7EcEi1y9A",
            "wwrtx.vid":"1688851045936785",
            "wwrtx.logined":"true"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def teardown_class(self):
        sleep(5)
        # self.driver.quit()

    def test_addmember(self):
        contact = ContactPage(self.driver)
        contact.add_member("tkn1", "tkn1", "13100000000", 0)

    def test_deletemember(self):
        pass
