from test_appium.base_page import BasePage


class SearchPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        self.driver.keyevent(66)
        self.sleep(3)
        return self
