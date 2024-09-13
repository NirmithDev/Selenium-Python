import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

os.environ['PATH'] += r"C:/Users/nirmi/SeleniumDrivers"
# Automation on web browser to open it for us
driver = webdriver.Chrome()
#How to handle inputs and form submission and result pages
driver.get("https://nirmithdev.github.io/")
#navigating by text
link=driver.find_element(By.LINK_TEXT,"Projects")
link.click()
try:
    #NAVIGATE to the project filter page
    element= WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "front"))
    )
    element.click()
    #time.sleep(5)
    #navigate back
    driver.back()
    link2 = driver.find_element(By.LINK_TEXT, "Contact")
    link2.click()
    time.sleep(5)
    # now we will click on the contact us button and have the dialog pop up with no messages
    link3 = driver.find_element(By.CLASS_NAME, "send-btn")
    link3.click()

    time.sleep(5)
finally:
    driver.quit()