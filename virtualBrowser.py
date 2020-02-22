# Python and Selenium!

from selenium import webdriver

#driver = webdriver.Chrome()

# specifiying where the driver is located on my pc
driver = webdriver.Chrome(executable_path='C:/Users/Cory/Documents/Code/Python_Selenium/ChromeDriver/chromedriver.exe')

driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

