import pytest
from PageObject.LoginPage import LoginPage
from utilities.ScreenshotUtils import save_screenshot

@pytest.mark.login
def test_login_flow(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Take screenshot after successful login
    save_screenshot(driver, "login_success")
