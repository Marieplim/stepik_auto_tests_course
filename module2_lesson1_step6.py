from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    sunduk = driver.find_element(By.ID, "treasure")
    treasure = sunduk.get_attribute("valuex")
    x = treasure
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    y_element = driver.find_element(By.ID, "answer")
    y_element.send_keys(y)
    option1 = driver.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = driver.find_element(By.ID, "robotsRule")
    option2.click()
    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()
finally:
    time.sleep(10)
    driver.quit()
    
