import pytest
from PageObject.LoginPage import LoginPage
from PageObject.ProductPage import ProductPage

def test_open_product_details_ios(driver):
    # Login first
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Open catalog and click product
    product_page = ProductPage(driver)
    product_page.open_product()  

    # Verify product name on details page
    name = product_page.verify_product_name()
    assert name == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack', got '{name}'"
