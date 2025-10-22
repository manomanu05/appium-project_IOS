import pytest
from PageObject.LoginPage import LoginPage
from PageObject.CatalogPage import CatalogPageIOS  # Use the iOS version

def test_add_product_to_cart_and_verify_ios(driver):
    # Login first
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Catalog actions for iOS
    catalog_page = CatalogPageIOS(driver)

    # Collect product text before adding to cart
    product_name_before = catalog_page.get_product_name_before()
    print(f"Product name before adding to cart: {product_name_before}")

    # Add product to cart
    catalog_page.add_to_cart()

    # Open cart
    catalog_page.open_cart()

    # Get product text in cart
    product_name_cart = catalog_page.get_cart_product_name()
    print(f"Product name in cart: {product_name_cart}")

    # Verify product names match
    assert product_name_before == product_name_cart, "Product name in cart does not match the selected product"
