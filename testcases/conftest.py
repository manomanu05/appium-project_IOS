from appium import webdriver
from appium.options.ios import XCUITestOptions
import pytest

@pytest.fixture(scope="class")
def setup_ios(request):
    options = XCUITestOptions()
    options.platformName = "iOS"
    options.deviceName = "iPhone 15"
    options.platformVersion = "17.0"
    options.automationName = "XCUITest"
    options.app = "/Users//Desktop/iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.7.1.ipa"
    options.noReset = True
    options.newCommandTimeout = 300

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", options=options)

    request.cls.driver = driver
    yield
    driver.quit()
