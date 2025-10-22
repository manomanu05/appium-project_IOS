from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.product_item = (
            AppiumBy.XPATH,
            '//XCUIElementTypeStaticText[@name="test-Item title" and @label="Sauce Labs Backpack"]'
        )
        self.product_name = (
            AppiumBy.XPATH,
            '//XCUIElementTypeStaticText[@name="Sauce Labs Backpack"]'
        )

    # Click product to open details
    def open_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_item)
        ).click()

    # Verify product name
    def verify_product_name(self):
        product = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_name)
        )
        return product.text
