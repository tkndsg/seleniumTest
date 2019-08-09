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
            "wwrtx.refid":"3019668238158576",
            "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d":"1565313991",
            "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d":"1565313991",
            "_ga":"GA1.2.234688722.1565313991",
            "_gid":"GA1.2.108200614.1565313991",
            "_gat":"1",
            "wwrtx.d2st":"a4824081",
            "wwrtx.sid":"ZRNJMZN4hWEA-UnHCIGv0y0WGzaZagu7EGkFidFp7InRgrMnEkiLH_voW87jHHho",
            "wwrtx.ltype":"1",
            "wxpay.corpid":"1970324979080668",
            "wxpay.vid":"1688851045936785",
            "wwrtx.vst":"9ULuEg7yRN4CVMX-O_wmYSFQnLuHSAClg21Cacc4axFfZ1odyvutaSwBy39nDlfQZF_bGSQO78cWuP47nPjYXHkN1D9AaLgaivc66fU-0Vz6BBC5bywwSktgApnihzVkrctQpPaeCU5I6QzO04qldw0onEQmlWqQgU1WYXXDyqGm525Ofj80sMrpqlMaXPoRQ4rMgruk9ENDr8sKSQXe8cIbJEYQfAcAwx1ZGyC1YylHpZvdHRf0IMksBtEdJKOBaPY0vcM3lMGUbE_ffSZHXw",
            "wwrtx.vid":"1688851045936785",
            "wwrtx.logined":"true"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()