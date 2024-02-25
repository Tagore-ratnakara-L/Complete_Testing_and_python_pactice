import time

import pytest
from selenium.webdriver.common.by import By


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username,password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])

    def test_negative_login(self, driver,username,password,expected_error_message):
        # open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        # Puch Submit button
        submitt_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submitt_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator.is_displayed(), "Error msg is nt displayed but it should be."

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_locator.text
        assert error_msg == expected_error_message, "Error msg is not expected."

        # open page
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(3)

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys(username)
        # username_locator.send_keys("student")

        # Type password incorrectPassword into Password field
        password_locator = driver.find_element(By.ID, "password")
        password_locator.send_keys(password)

        # Puch Submit button
        submitt_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submitt_button_locator.click()
        time.sleep(3)

        # Verify error message is displayed
        error_msg_locator = driver.find_element(By.ID, "error")
        assert error_msg_locator.is_displayed(), "Error msg is nt displayed but it should be."

        # Verify error message text is Your username is invalid!
        error_msg = error_msg_locator.text
        assert error_msg == expected_error_message, "Error msg is not expected."
