# Open page
# Type username student into Username field
# Type password incorrectPassword into Password field
# Puch Submit button
# Verify error message is displayed
# Verify error message text is Your password is invalid!

import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    print("creating chrome driver")
    my_driver = webdriver.Chrome()
    yield my_driver
    print("Closing chrome driver")
    my_driver.quit()


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self,driver):
        # open page
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")
        # username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys("incorrectPassword")

        # Puch Submit button
        submitt_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submitt_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator.is_displayed(), "Error msg is nt displayed but it should be."

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_locator.text
        assert error_msg == "Your password is invalid!", "Error msg is not expected."
