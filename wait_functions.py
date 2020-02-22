# Sometimes a Wait is need in order to Wait for a website 
# to wait for an element to load due to AJAX techniques

# 2 types of Waits

# 1. Explict Wait Functions, Will wait until a condition is met
# 2. Implicit Wait Functions, Pull DOM for a certian amount of time, until element becomes available

from selenium import webdriver
from selenium.driver.commmon.by import By
from selenium.driver.support.ui import WebDriverWait
from selenium.driver.support import expected_conditions as EC

# specifiying where the driver is located on my pc
driver = webdriver.Chrome(executable_path='C:/Users/Cory/Documents/Code/Python_Selenium/ChromeDriver/chromedriver.exe')

    # Maximize the window
    #driver.maximize_window()

# using this site for practice
driver.get('https://google.com/earth')

# now using an explicit wait, 10 seconds
wait = WebDriverWait(driver, 10)

launch_earth_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))

launch_earth_button.click()