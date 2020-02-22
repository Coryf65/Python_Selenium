# Python and Selenium!

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# specifiying where the driver is located on my pc
driver = webdriver.Chrome(executable_path='C:/Users/Cory/Documents/Code/Python_Selenium/ChromeDriver/chromedriver.exe')

    # Maximize the window
    #driver.maximize_window()

# using this site for practice
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# source element
source_box = driver.find_element_by_xpath('//*[@id="box3"]')

# destination element
dest_box = driver.find_element_by_xpath('//*[@id="box103"]')

# to use a Drag And Drop need to add lib (Action Chains)
actions = ActionChains(driver)

actions.drag_and_drop(source_box, dest_box).perform()
