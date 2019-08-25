from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


def driver():
    caps = {}
    caps["platformName"] = "Android"
    caps["deviceName"] = "Meizu16x"
    caps["appPackage"] = "com.xueqiu.android"
    caps["appActivity"] = ".view.WelcomeActivityAlias"
    caps["autoGrantPermissions"] = True
    driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
    return driver
