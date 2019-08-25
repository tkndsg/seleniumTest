from selenium.common.exceptions import NoSuchElementException

from test_po.base_page import BasePage


class CommonUtil(BasePage):
    def isElementExist(self, by, locator):
        flag = None
        self.sleep(1)
        try:
            self.driver.find_element(by,locator)
            flag = True
        except NoSuchElementException:
            flag = False
        finally:
            return flag
