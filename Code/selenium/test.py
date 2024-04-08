import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DaterLoginTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://localhost:8000')
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.assertIn('Cupid Code', self.browser.title)

    def test_dater_login(self):
        self.browser.find_element(By.ID, 'login').click()
        self.browser.find_element(By.ID, 'email').send_keys('bob@cupidcode.com')
        self.browser.find_element(By.ID, 'password').send_keys('password')
        self.browser.find_element(By.ID, 'sign_in').click()


if __name__ == '__main__':
    unittest.main(verbosity=2)
