from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

link = "http://suninjuly.github.io/selects2.html"

try:
	driver = webdriver.Chrome()
	driver.get(link)
	x_element = driver.find_element(By.ID, "num1")
	y_element = driver.find_element(By.ID, "num2")
	x = x_element.text
	y = y_element.text
	number = str(int(x) + int(y))
	select = Select(driver.find_element(By.ID, "dropdown"))
	select.select_by_value(str(number))
	button = driver.find_element(By.CLASS_NAME, "btn")
	button.click()
	
finally:
	time.sleep(10)
	driver.quit()
    
