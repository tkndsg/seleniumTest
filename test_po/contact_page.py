from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class ContactPage:

    def __init__(self,wework):
        self.driver = wework.driver

    def add_member(self,name, username, phone, ssm,**kwargs):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        sleep(5)
        flag = self.whichflag("37")
        self.driver.find_element(By.XPATH, '//*[@id="js_contacts'+flag+'"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]').click()

        sleep(2)
        # 上传头像
        img = self.driver.find_element(By.XPATH, '//*[@id="js_upload_file"]/div/div[2]')
        #todo change to a function
        self.driver.execute_script("arguments[0].click()", img)
        sleep(2)
        uploadimg = self.driver.find_element(By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[2]/div/div[1]/div[2]/a/input')
        uploadimg.send_keys("G:\Program Files\JetBrains\etransfer\images\cat.jpg")
        # uploadimg.send_keys("E:\PythonWorkSpace\seleniumTest\images\cat.jpg")

        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="__dialog__avatarEditor__"]/div/div[3]/a[1]').click()
        sleep(3)

        #填写信息
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(name)
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(username)
        self.driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        sleep(2)

        #下滑页面，点保存按钮
        self.driver.execute_script("window.scrollBy(0,300)")
        sleep(2)
        if ssm == 0:
            self.driver.find_element(By.XPATH, '//*[@id="js_contacts'+flag+'"]/div/div[2]/div/div[4]/div/form/div[2]/div[5]/div/div[2]/label/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="js_contacts'+flag+'"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        return self

    def delete_member(self):
        pass

    def get_tips(self):
        return "OK"

    def whichflag(self,flag):
        try:
           element = self.driver.find_element(By.XPATH, '//*[@id="js_contacts'+flag+'"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')
           return flag
        except NoSuchElementException as e:
            print("报错了，说明不是37，变成了38")
            flag = "38"
            return flag

