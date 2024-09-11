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
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#the text input box
element_first_text = driver.find_element(By.NAME, 'my-text')
element_first_text.send_keys("Selenium")
#time.sleep(25)
#the password box
#CSS selectors is also a valid option to
element_password = driver.find_element(By.NAME, 'my-password')
element_password.send_keys("SecretPassword")

element_password_value = element_password.get_attribute('value')
print(element_password_value)
#time.sleep(25)
#textarea
element_textarea = driver.find_element(By.NAME, 'my-textarea')
element_textarea.send_keys("This is a text area data")
element_textarea_value = element_textarea.get_attribute('value')
#print(element_textarea_value)
#check if the input is disabled
if(driver.find_element(By.NAME,'my-disabled').get_attribute('disabled')):
    print("This input is disabled")

#check if the input is read only
if(driver.find_element(By.NAME,'my-readonly').get_attribute('readonly')):
    print("This input is read only")

#Dropdown data and select and verify the data is there
element_dropdown=Select(driver.find_element(By.NAME,'my-select'))
element_dropdown.select_by_visible_text("One")
#verify this is the value
element_dropdown_value = driver.find_element(By.NAME,'my-select').get_attribute('value')
print(element_dropdown_value)

#Dropdown datalist
element_dropdownlist=driver.find_element(By.NAME,'my-datalist')
element_dropdownlist.send_keys('San Francisco')

option=WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME,'my-datalist'))
)
option.click()
#verify this is the value
element_dropdownList_value = driver.find_element(By.NAME,'my-datalist').get_attribute('value')
print(element_dropdownList_value)

#File Input choose a dummy file and upload ig
file_input = driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_path = os.path.join(r"C:/Users/nirmi/OneDrive/Desktop", "randomTest.txt")
file_input.send_keys(file_path)
#value verification for the data
file_input_value = driver.find_element(By.CSS_SELECTOR,"input[type='file']").get_attribute('value')
print(file_input_value)

#checkbox and testing
    #check them if it is unchecked
    #uncheck them if it is checked then verify

checkbox = driver.find_element(By.ID,'my-check-1')
if not checkbox.is_selected():
    checkbox.click()
else:
    checkbox.click()
    print("Checked box is deselected")

decheckbox = driver.find_element(By.ID,'my-check-2')
if not decheckbox.is_selected():
    decheckbox.click()
    print("Checked box is selected")
else:
    decheckbox.click()
    print("Checked box is deselected")

#submit button click when all data is filled in
submitButton = driver.find_element(By.CLASS_NAME,'btn-outline-primary')
submitButton.click()
#color picker choose some random ahh color


#Date Picker select today
#date_picker_input = driver.find_element(By.NAME, 'my-date')  # Use class name to find the input field
#date_picker_input.click()
'''next_button = driver.find_element(By.CLASS_NAME, 'datepicker-next')  # This might be specific to your calendar
while True:
    # Check the currently displayed month and year
    displayed_month = driver.find_element(By.CLASS_NAME, 'datepicker-switch').text

    # Break out when the correct month and year is found
    if "September 2024" in displayed_month:
        break

    next_button.click()
    time.sleep(1)
'''
# Select the desired day, e.g., 15th of September 2024
# Use XPath to target the specific day number
#day = driver.find_element(By.XPATH, "//td[@class='day' and text()='15']")
#day.click()
#Example Range


time.sleep(5)
driver.quit()