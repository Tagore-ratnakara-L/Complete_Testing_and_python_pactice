from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
import time

# This is for chrome
# # chrome driver - Chrome browser
# # Method-1
# service_obj = Service()  # SeleniumManager
# driver = webdriver.Chrome(service=service_obj)
# driver.maximize_window()
# driver.get("https://python.org")
# driver.minimize_window()
# # prints page title
# print(driver.title)  # Welcome to Python.org
# # prints directed url
# print(driver.current_url)  # https://www.python.org/
# driver.maximize_window()
# driver.get("https://python.org")
# driver.back()
# driver.refresh()
# driver.forward()
# time.process_time()
# # Method-2
# # driver = webdriver.Chrome()
# # driver.get("https://python.org")
# time.sleep(5)
# driver.close()

service_obj = Service()  # SeleniumManager
driver = webdriver.Edge(service=service_obj)
driver.maximize_window()
driver.get("https://python.org")
driver.minimize_window()
# prints page title
print(driver.title)  # Welcome to Python.org
# prints directed url
print(driver.current_url)  # https://www.python.org/
driver.maximize_window()
driver.get("https://python.org")
driver.back()
driver.forward()
driver.refresh()
time.process_time()
time.sleep(4)
# Method-2
# # driver = webdriver.Edge()
# # driver.get("https://python.org")
# time.sleep(5)
# driver.close()
