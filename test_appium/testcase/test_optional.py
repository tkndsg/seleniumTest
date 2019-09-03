import pytest

from test_appium.pages.xueqiu_page import XueqiuPage


class TestOptional:
    def setup_class(self):
        self.xueqiu = XueqiuPage()

    def teardown_class(self):
        self.xueqiu.sleep(5)
        self.xueqiu.driver.quit()

    @pytest.mark.parametrize("keyword, stock_name, symbol",[("alibaba", "阿里巴巴", "BABA"), ("xiaomi", "小米集团-W", "01810"), ("google", "谷歌", "GOOGL")])
    def test_addoptional(self, keyword, stock_name, symbol):
        self.xueqiu.goto_optional().goto_search().search(keyword).addoptional(symbol).back_to_xuqiu()
        assert stock_name, symbol in self.xueqiu.driver.page_source
        self.xueqiu.driver.keyevent(4)

    @pytest.mark.parametrize("keyword, stock_name, symbol", [("alibaba", "阿里巴巴", "BABA"), ])
    def test_dropoptional_search(self, keyword, stock_name, symbol):
        self.xueqiu.goto_optional().goto_search().search(keyword).dropoptional(symbol).back_to_xuqiu()
        assert stock_name, symbol not in self.xueqiu.driver.page_source

    @pytest.mark.parametrize("keyword, stock_name, symbol", [("xiaomi", "小米集团-W", "01810"), ])
    def test_dropoptional_longclick(self, keyword, stock_name, symbol):
        # todo 自选页面，增加长按股票删除自选测试用例
        self.xueqiu.goto_optional().goto_search().search(keyword).dropoptional(symbol).back_to_xuqiu()
        assert stock_name, symbol not in self.xueqiu.driver.page_source

