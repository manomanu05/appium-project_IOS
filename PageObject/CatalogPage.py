from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CatalogPageIOS:
    def __init__(self, driver):
        self.driver = driver
        # Locators for iOS (d XPaths)
        self.product_name_before = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="test-Item title" and @label="Sauce Labs Backpack"]')
        self.add_to_cart_button = (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="ADD TO CART"])[1]')
        self.cart_icon = (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="test-Cart"]/XCUIElementTypeOther')
        self.cart_product_name = (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Sauce Labs Backpack"]')

    # Get product text before adding to cart
    def get_product_name_before(self):
        product_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.product_name_before)
        )
        return product_element.label  # iOS uses .label instead of .text

    # Add product to cart
    def add_to_cart(self):
        add_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_btn.click()

    # Open cart
    def open_cart(self):
        cart_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        cart_btn.click()

    # Get product text in cart
    def get_cart_product_name(self):
        cart_product = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.cart_product_name)
        )
        return cart_product.label  # .label
