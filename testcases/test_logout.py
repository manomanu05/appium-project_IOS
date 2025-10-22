import pytest
from PageObject.LoginPage import LoginPage
from PageObject.HomePage import HomePage

def test_login_and_logout(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    home_page = HomePage(driver)
    home_page.logout()
