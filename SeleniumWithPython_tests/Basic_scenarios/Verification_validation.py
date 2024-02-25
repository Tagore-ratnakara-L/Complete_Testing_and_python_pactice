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
username_locator.send_keys("student")

# Step-3 Type password Password123 into Password field
password_locator = driver.find_element(By.ID, "password")
password_locator.send_keys("Password123")

# Step-4 Push Submit button
submitt_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
submitt_button_locator.click()
time.sleep(3)

# Step-5 Verify new page URL contains practicetestautomation.com/logged-in-successfully/
Current_url = driver.current_url
print(Current_url)
# compare the actual url with loading in boolean
assert Current_url == "https://practicetestautomation.com/logged-in-successfully/"

# Step-6 Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = driver.find_element(By.TAG_NAME,"h1")
actual_text = text_locator.text
# compare the actual text with loading text in boolean
assert actual_text == "Logged In Successfully"


#This case is sucessfull since we are  logged in h1 tag exists in 2nd page after login

# Step-7 Verify button Log out is displayed on the new page
verify_logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
# compare the verify_logout_button_locator with Log out in boolean
assert verify_logout_button_locator.is_displayed()