from selenium import webdriver


class WeworkPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        cookies = {
            "wwrtx.sid":"ZRNJMZN4hWEA-UnHCIGv0wapF7HwezZ_YPiwXqvUe_mpPpQDRSrhFNA6_yBnUAOG"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()