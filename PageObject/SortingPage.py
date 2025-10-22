from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class SortingPageIOS:
    def __init__(self, driver):
        self.driver = driver
        # D XPath for filter/sort button in iOS
        self.filter_button = (AppiumBy.XPATH,
                              '//XCUIElementTypeButton[@name="test-Modal Selector Button"]')

    def open_filter_modal(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.filter_button)
        ).click()

    def select_price_low_to_high(self, screenshot_path="screenshots/price_low_to_high_ios.png"):
        # Dummy XPath for "Price (low to high)" option in iOS
        option_xpath = '//XCUIElementTypeStaticText[@name="Price (low to high)"]'
        option = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, option_xpath))
        )
        option.click()

        # Take screenshot after sorting
        os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
        self.driver.get_screenshot_as_file(screenshot_path)
        print(f"Screenshot saved at: {screenshot_path}")
