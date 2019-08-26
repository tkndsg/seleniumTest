from test_appium.base_page import BasePage
from test_appium.search_page import SearchPage


class OptionalPage(BasePage):
    def goto_search(self):
        self.driver.find_element_by_id("search_input_text")
        return SearchPage(self.driver)

    def addoptional(self):
        if self.is_element_exist("xpath", "//*[@text='BABA']/../../..//*[@text='加自选']"):
            self.driver.find_element_by_xpath("//*[@text='BABA']/../../..//*[@text='加自选']").click()
            if self.is_element_exist("xpath", "//*[@text='下次再说']"):
                self.driver.find_element_by_xpath("//*[@text='下次再说']").click()
        return self

    def dropoptional(self):
        return self
