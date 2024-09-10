import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] += r"C:/Users/nirmi/SeleniumDrivers"

# Automation on web browser to open it for us
driver = webdriver.Chrome()

# Specify the website URL
driver.get("https://jqueryui.com/progressbar/#download")

# Switch to the iframe that contains the button
iframe = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(iframe)
driver.implicitly_wait(15)
# Now you can find and click the button
my_element = driver.find_element(By.ID, 'downloadButton')
my_element.click()
#time.sleep(15)

#complete_element=driver.find_element(By.CLASS_NAME,'progress-label')
#print(f"{complete_element.text == 'Complete!'}")
#filtration Element and expected Text
WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME,'progress-label'),'Complete!'
    )
)

# Close the browser
driver.quit()