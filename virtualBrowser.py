# Python and Selenium!
from selenium import webdriver

# specifiying where the driver is located on my pc
driver = webdriver.Chrome(executable_path='C:/Users/Cory/Documents/Code/Python_Selenium/ChromeDriver/chromedriver.exe')

# using this site for practice
driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

# going to try type and click a button using python
message_field = driver.find_element_by_xpath('//*[@id="user-message"]')

# adding my text
message_field.send_keys('Hello World!')

# this is using X-Path, find using dev tools in browser and right click and copy xpath by an element in the DOM
show_message_button = driver.find_element_by_xpath('//*[@id="get-input"]/button')

# now forcing a click
show_message_button.click()

# Now handling Input fields
input_1 = driver.find_element_by_xpath('//*[@id="sum1"]')

# adding text
input_1.send_keys('10')

input_2 = driver.find_element_by_xpath('//*[@id="sum2"]')

# 2nd text input
input_2.send_keys('50')

# get total button
total_button = driver.find_element_by_xpath('//*[@id="gettotal"]/button')

total_button.click()