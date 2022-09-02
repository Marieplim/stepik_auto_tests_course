from selenium import webdriver
from selenium.webdriver.common.by import By

import os
import time

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()

try:
	browser.get(link)
	element_name = browser.find_element(By.NAME, "firstname")
	element_name.send_keys("Maria")
	element_surname = browser.find_element(By.NAME, "lastname")
	element_surname.send_keys("Babich")
	element_email = browser.find_element(By.NAME, "email")
	element_email.send_keys("ooooooooooo")
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'test1.txt')
	element = browser.find_element(By.ID, "file")
	element.send_keys(file_path)
	button = browser.find_element(By.CLASS_NAME, "btn")
	button.click()

finally:
	time.sleep(5)
	browser.quit()
