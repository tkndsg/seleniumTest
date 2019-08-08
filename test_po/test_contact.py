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
            "wwrtx.i18n_lan_key": "zh-CN%2Czh%3Bq%3D0.9",
            "wwrtx.i18n_lan": "zh-cn",
            "wwrtx.ref": "direct",
            "wwrtx.refid": "5198630543370780",
            "_ga": "GA1.2.1494591535.1565225775",
            "_gid": "GA1.2.585569866.1565225775",
            "_gat": "1",
            "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d": "1565225775",
            "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d": "1565225775",
            "wwrtx.d2st": "a5757871",
            "wwrtx.sid": "ZRNJMZN4hWEA-UnHCIGv024SR9TDpm8jXW1jAh2EAqE5J0kvA5b9KKyQQwlIT4-g",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324979080668",
            "wxpay.vid": "1688851045936785",
            "wwrtx.vst": "bHo4mzyyQFXgZUbGVHqH3Rw0d3XzeiyrZgjHO2bMYB_jzsKrPBPtOdTMBj_eADMv__XZGqZzN-bOQNDneTkFtZtWsj3Q9xanNkQQJm27Hvbrn02FC31MNKshl86MvP2Ek0GGT3pCAI4NjRMEcUndFJtHsf0EWo4N9LKWU4l_-wyqihfl9r17dwofeT070FGbvpPjQZRZ3qy2zhJiUA7vp_uIzxniBtooUy2qvjUSWPy3ePiBw2P_eGhP9TnTCniYWRLjTqo2vLNBMKOMDvpRNQ",
            "wwrtx.vid": "1688851045936785",
            "wwrtx.logined": "true"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    def test_addmember(self):
        contact = ContactPage(self.driver)
        contact.add_member("tkn1", "tkn1", "13100000000", 0)

    def test_deletemember(self):
        pass
