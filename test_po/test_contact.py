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
            "wwrtx.refid": "536640270819298",
            "_ga": "GA1.2.1873791945.1565277221",
            "_gid": "GA1.2.1290005412.1565277221",
            "_gat": "1",
            "wwrtx.d2st": "a4022652",
            "wwrtx.sid": "ZRNJMZN4hWEA-UnHCIGv0_JsAsZRhVGmSo5x5S-Z2DaIgWX2upFmDNdShmCzurhJ",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324979080668",
            "wxpay.vid": "1688851045936785",
            "wwrtx.vst": "Df0RPEabL9ILAoroDmhPD8llyGjGJcbu9nuvZdibd0IHpZ_q6xJzBWKeg-zIihp74L7qPkfm23SfFnYhnJNslAIfyx0wQS9yGEOhnjvvFChQpc1AiPXoiC8fmRXk-7sk4i3f4Ze_l-fa0gFP3P2I-PXgP4m80jdoB3RdIbkCQROsAjxTbNtAlcpZc1tc-PlAs_xFEfGqXJpmYOVGVKPc_J5IljEE6d3iJTGnDidbLHwCJejSwRLFcqma_tfHcAomQdCwyDnKQ8m03PzjkeiR0g",
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
