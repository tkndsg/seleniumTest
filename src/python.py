def test_001():
    tips = "111"
    loct = "//*[contains(@text,'"+tips+"')]"
    print(loct)


def test_02():
    symbol = "tkn"
    print("//*[@text=%s/../../..//*[@text='加自选']" % symbol)
