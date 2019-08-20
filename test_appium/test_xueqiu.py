from time import sleep

from appium import webdriver


class TestLogin:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "Meizu16x"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    def test_wrong_phone(self):
        el1 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ImageView")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/iv_login_phone")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_login_with_account")
        el3.click()
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/login_account")
        el4.send_keys("9999999999999999")
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/login_password")
        el5.send_keys("123456")
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/button_next")
        assert "手机号码填写错误" in self.driver.page_source
        el6.click()

    def test_wrong_password(self):
        el4 = self.driver.find_element_by_id("com.xueqiu.android:id/login_account")
        el4.send_keys("13169646666")
        el5 = self.driver.find_element_by_id("com.xueqiu.android:id/login_password")
        el5.send_keys("123456")
        el6 = self.driver.find_element_by_id("com.xueqiu.android:id/button_next")
        assert "用户名或密码错误" in self.driver.page_source
        el6.click()
        self.driver.find_element_by_id("iv_action_back").click()
        self.driver.find_element_by_id("md_buttonDefaultNegative").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.ImageView").click()
