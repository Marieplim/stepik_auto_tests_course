from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/execute_script.html"

try:
	browser.get(link)
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	def calc(x):
			return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)
	button = browser.find_element(By.CLASS_NAME, "btn")
	browser.execute_script("window.scrollBy(0, 100);")
	c = browser.find_element(By.ID, "answer")
	c.send_keys(y)
	robot_1 = browser.find_element(By.ID, "robotCheckbox")
	robot_1.click()
	robot_2 = browser.find_element(By.ID, "robotsRule")
	robot_2.click()
	button.click()
finally:
	time.sleep(5)
	browser.quit()

