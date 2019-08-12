from selenium import webdriver


class WeworkPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        cookies = {
            "wwrtx.i18n_lan_key": "zh-CN%2Czh%3Bq%3D0.9",
            "wwrtx.i18n_lan": "zh-cn",
            "wwrtx.ref": "direct",
            "wwrtx.refid": "12917460622687923",
            "Hm_lvt_9364e629af24cb52acc78b43e8c9f77d": "1565613889",
            "Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d": "1565613889",
            "_ga": "GA1.2.915025705.1565613889",
            "_gid": "GA1.2.1898391055.1565613889",
            "_gat": "1",
            "wwrtx.d2st": "a1158000",
            "wwrtx.sid": "ZRNJMZN4hWEA-UnHCIGv07B9QaPOkTCTOr0ksFMwhwGLUaVBWntNfF-zqpHovWux",
            "wwrtx.ltype": "1",
            "wxpay.corpid": "1970324979080668",
            "wxpay.vid": "1688851045936785",
            "wwrtx.vst": "VNZSSJxrUTlWYmjuzGxZvSsRBgXf3xW9o9twVTvZH5OE7ryfKk816oyXqeEx4F98muY04d0QWLDzzbXoqDwvwbVKwtemKw6X6QvY1k9kGrXHP4Ftl27zmnHegNO9AlfXj71sKWe1OmO21x6KXO4UTl6-fPd9STWRUt5RUL411eE1QJRSPNjkCkpNmVI9ueIzrHTUgF2oAIcwJHaQFSED7olY7Ml1S0hx2-R1Ci60kkGMxZB4kOBshPEu5t5a8MKWLjzN-iALZnGKY-EZcFhdEg",
            "wwrtx.vid": "1688851045936785",
            "wwrtx.logined": "true"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()