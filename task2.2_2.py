from selenium import webdriver
from selenium.webdriver.common.by import By

import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)


button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
x = browser.find_element(By.ID, "input_value")
x = x.text
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, '[id="answer"]')
input1.send_keys(y)

checkb = browser.find_element(By.CSS_SELECTOR, '.form-check-input')
checkb.click()

radiob = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true)", radiob)
radiob.click()

browser.execute_script("return arguments[0].scrollIntoView(true)", button)
button.click()

time.sleep(5)
browser.quit()

