from selenium import webdriver
import time
# from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@class='btn']").click()
driver.minimize_window()
time.sleep(4)
driver.close()

driver = webdriver.Edge()
driver.maximize_window()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[@class='btn']").click()
driver.minimize_window()
time.sleep(4)
driver.close()
