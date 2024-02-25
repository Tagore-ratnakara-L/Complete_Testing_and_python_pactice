# """Test case 1: Positive LogIn test"""
# Step-1 Open page
# Step-2 Type username student into Username field
# Step-3 Type password Password123 into Password field
# Step-4 Push Submit button
# Step-5 Verify new page URL contains practicetestautomation.com/logged-in-successfully/
# Step-6 Verify new page contains expected text ('Congratulations' or 'successfully logged in')
# Step-7 Verify button Log out is displayed on the new page

# Step-1 Open page
import time
#time library will automatically added to the script from python libraries
from selenium import webdriver
from selenium.webdriver.common.by import By

#open web browser
driver = webdriver.Chrome()
time.sleep(2) #opens browser and waits for 5 seconds

#Go to web page
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(3) # calls URL and remains for 10 seconds after rendering and closes

# Step-2 Type username student into Username field
username_locator = driver.find_element(By.ID, "username")

# Step-3 Type password Password123 into Password field
password_locator = driver.find_element(By.ID, "password")

# Step-4 Push Submit button
submitt_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")

# Step-5 Verify new page URL contains practicetestautomation.com/logged-in-successfully/

# Step-6 Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME,"h1")
#This case failed since we are not logged in yet h1 tag exists in 2nd page after login

# Step-7 Verify button Log out is displayed on the new page
verify_logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")