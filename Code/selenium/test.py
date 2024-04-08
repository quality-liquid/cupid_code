import unittest
from selenium import webdriver


class DaterLoginTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Cupid Code', self.browser.title)

    def test_dater_login(self):
        self.browser.find_element(By.NAME, 'a').send_keys('bob@cupidcode.com')


if __name__ == '__main__':
    unittest.main(verbosity=2)
