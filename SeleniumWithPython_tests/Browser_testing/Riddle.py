from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://techstepacademy.com/trial-of-the-stones")
driver.maximize_window()
ROStone = driver.find_element(By.ID, "r1Input")
ROStone.send_keys('rock')
time.sleep(2)
BTN1 = driver.find_element(By.ID, "r1Btn")
BTN1.click()
time.sleep(2)
ROSecret = driver.find_element(By.ID, "r2Input")
ROSecret.send_keys("bamboo")
time.sleep(2)
BTN2 = driver.find_element(By.ID, "r2Butn")
BTN2.click()
# RichMerch = driver.find_element(By.XPATH, "//b[normalize-space()='Jessica']")
# RMerch = RichMerch.text
elem1 = driver.find_element(By.XPATH, "//p[normalize-space()='3000']")
elem2 = driver.find_element(By.XPATH, "//p[normalize-space()='2000']")
if elem1.text > elem2.text:
    RMerch = driver.find_element(By.XPATH,"//b[normalize-space()='Jessica']").text
else:
    RMerch = driver.find_element(By.XPATH,"//b[normalize-space()='Bernard']").text
time.sleep(2)
TwoMerch = driver.find_element(By.ID, "r3Input")
TwoMerch.send_keys(RMerch)
time.sleep(2)
BTN3 = driver.find_element(By.ID, "r3Butn")
BTN3.click()
time.sleep(2)
FinalBTN = driver.find_element(By.ID, "checkButn")
FinalBTN.click()
RiddleOut = driver.find_element(By.CSS_SELECTOR, "div#trialCompleteBanner")
assert RiddleOut.text == 'Trial Complete', "Values doesn't matched"
time.sleep(4)
driver.close()
driver.quit()

