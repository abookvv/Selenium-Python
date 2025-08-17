import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestsOnWebpages(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def fill_form(self, link):
        self.browser.get(link)

        self.browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Petrov")
        self.browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("email@example.com")
        self.browser.find_element(By.CSS_SELECTOR, ".second_block .first").send_keys("+123456789")
        self.browser.find_element(By.CSS_SELECTOR, ".second_block .second").send_keys("Moscow")

        # Отправляем форму
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        # Ждем результат регистрации
        welcome_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h1"))
        ).text
        return welcome_text

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        registration_result = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        registration_result = self.fill_form(link)
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)


if __name__ == "__main__":
    unittest.main()