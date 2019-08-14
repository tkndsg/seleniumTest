from selenium import webdriver


class WeworkPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.maximize_window()
        cookies = {
            "wwrtx.sid":"ZRNJMZN4hWEA-UnHCIGv051rEfsBxpk4XGiQbQaNQsZJQsu1TTQ3ICQ3o7gRgTAp"
        }
        for k, v in cookies.items():
            self.driver.add_cookie({"name":k, "value":v})
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def quit(self):
        self.driver.quit()
