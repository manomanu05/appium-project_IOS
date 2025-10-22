import pytest
from PageObject.LoginPage import LoginPage
from appium.webdriver.common.appiumby import AppiumBy
import os
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from utilities.ScreenshotUtils import save_screenshot


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    # Attempt invalid login
    login_page.login("invalid_user", "wrong_password")

    try:
        error_msg = driver.find_element(
            AppiumBy.XPATH,
            '//XCUIElementTypeStaticText[@name="Username and password do not match any user in this service."]'
        )
        if error_msg.is_displayed():
            save_screenshot(driver, "invalid_login_ios")
    except NoSuchElementException:
        pass
