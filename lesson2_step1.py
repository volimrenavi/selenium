from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, 'img')
    input1_1=input1.get_attribute("valuex")
    y = calc(input1_1)
    input0=browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
    input0.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR,'[type="checkbox"]')
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, '[value="people"]')
    input3.click()
    input4 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    input4.click()
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
finally:
    time.sleep(20)
    browser.quit()