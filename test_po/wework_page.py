from selenium import webdriver


class WeworkPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        cookies = {
            "wwrtx.i18n_lan_key":"zh-CN%2Czh%3Bq%3D0.9",
            "wwrtx.i18n_lan":"zh-cn",
            "wwrtx.ref":"direct",
            "wwrtx.refid":"3019668238119139",
            "_ga":"GA1.2.1501597677.1565335196",
            "_gid":"GA1.2.1233489578.1565335196",
            "_gat":"1",
            "wwrtx.d2st":"a753841",
            "wwrtx.sid":"ZRNJMZN4hWEA-UnHCIGv08uB1WJBxaaZ61gLBedAgHgR1bAeCSthmsDvzmIxttZr",
            "wwrtx.ltype":"1",
            "wxpay.corpid":"1970324979080668",
            "wxpay.vid":"1688851045936785",
            "wwrtx.vst":"ZhhLTEIfPCbb6bKz7EVjL1_SLAUuB-eP2PimebBvbmltDvb9mKAHAFS5yJ-1IFCOliFv89kMtjbAuz8R_0xosWHquMGMO3V_uQOBghNToW7shMTYMAwi40j4_6Bj1aV2Jh1L7Y9nNYIqStyEMZG-ciPPB9-XbmXF4DnTAJ4OWNT_cjKU6d7ie5-RhpKzmkCifRiXj6SnOvkeY85jvH17E7Es1Nvob13kUKJyf8wFwkSmuW_Y_D2R1vv7Neu93sR9qkecbxSPAXfj4pUtDv-cfQ",
            "wwrtx.vid":"1688851045936785",
            "wwrtx.logined":"true"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()