#open browser
import time
#time library will automatically added to the script from python libraries
from selenium import webdriver

#open web browser
driver = webdriver.Chrome()
time.sleep(5) #opens browser and waits for 5 seconds

#Go to web page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(10) # calls URL and remains for 10 seconds after rendering and closes