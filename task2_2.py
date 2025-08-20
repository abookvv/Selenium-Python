from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    name = browser.find_element(By.NAME, "firstname")
    surname = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    file_upload = browser.find_element(By.NAME, "file")
    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")

    name.send_keys("Name")
    surname.send_keys("Surname")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_upload.send_keys(file_path)

    button.click()


finally:
    time.sleep(5)
    browser.quit()