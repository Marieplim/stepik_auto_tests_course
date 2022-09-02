from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Chrome()

try:
	browser.get(link)
	button1 = browser.find_element(By.CLASS_NAME, "btn")
	button1.click()
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)
	answer_element = browser.find_element(By.ID, "answer")
	answer_element.send_keys(y)
	button = browser.find_element(By.CLASS_NAME, "btn")
	button.click()
finally:
	time.sleep(40)
	browser.quit()
