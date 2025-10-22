import os
from datetime import datetime


def save_screenshot(driver, name="screenshot"):

    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    print(f"Screenshot saved to {path}")
