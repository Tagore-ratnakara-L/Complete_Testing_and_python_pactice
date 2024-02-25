from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input#userPassword").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "input#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#---------------------------------------------------------------------------------#

driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()

time.sleep(3)
driver.close()
