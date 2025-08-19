from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 13).until(
  EC.text_to_be_present_in_element((By.ID, "price"), "100")
)
button_book = browser.find_element(By.ID, "book").click()

x = browser.find_element(By.ID, "input_value").text
res = calc(x)

answer_input = browser.find_element(By.ID, "answer")
answer_input.send_keys(res)

button_submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button_submit.click()

time.sleep(5)
browser.quit()

