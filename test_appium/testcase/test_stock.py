class TestSearch:
    def setup_class(self):
        self.driver = driver()
        self.xueqiu = XueqiuPage(self.driver)
        self.search = SearchPage(self.driver)

    def teardown_class(self):
        sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("key, name", [("alibaba", "阿里巴巴"), ("xiaomi", "小米"), ("google", "谷歌")])
    def test_search(self,key,name):
        self.xueqiu.goto_search().search(key)
        assert name in self.driver.page_source
        self.search.back_to_xuqiu()
