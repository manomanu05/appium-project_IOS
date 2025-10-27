import pytest
from PageObject.LoginPage import LoginPage
from PageObject.SortingPage import SortingPageIOS  # iOS page object

def test_login_and_apply_filter_ios(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    #  Open filter modal
    sorting_page = SortingPageIOS(driver)
    sorting_page.open_filter_modal()

    #  Select "Price (low to high)"
    sorting_page.select_price_low_to_high()
