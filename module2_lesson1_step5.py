from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"

import time
import math

try:
    driver = webdriver.Chrome()
    driver.get(link)
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    y_element = driver.find_element(By.ID, "answer")
    y_element.send_keys(y)
    option1 = driver.find_element(By.CSS_SELECTOR, '[for=robotCheckbox]')
    option1.click()
    option2 = driver.find_element(By.CSS_SELECTOR, "[value = 'robots']")
    option2.click()
    button = driver.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(5)
    driver.quit()

