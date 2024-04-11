import sys
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

import utils


class LoginTestCases(unittest.TestCase):

    def setUp(self):
        chrome, headless = utils.flagParse()
        if not chrome:
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('-headless')
            self.browser = webdriver.Firefox(options=options)
        else:
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
            self.browser = webdriver.Chrome(options=options)

        self.browser.get('http://localhost:8000')
        self.browser.find_element(By.ID, 'login').click()
        self.addCleanup(self.browser.quit)

    def test_dater(self):
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/home/1')
        self.browser.find_element(By.ID, 'djHideToolBarButton').click()
        self.browser.find_element(By.ID, 'profile').click()
        inputs = self.browser.find_elements(By.TAG_NAME, 'input')

        # Test
        expected = ['Bob', 'The Builder', '1234567890',
                    '41.74291256257548, -111.83084429426646', 'dater1', 'bob@cupidcode.com']
        for i in range(len(expected)):
            # inputs[0] will be csrf token, so inputs will be offset by 1
            self.assertEqual(expected[i], inputs[i+1].get_attribute('value'))

    def test_cupid(self):
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.browser.find_element(By.ID, 'djHideToolBarButton').click()
        self.browser.find_element(By.ID, 'profile').click()
        inputs = self.browser.find_elements(By.TAG_NAME, 'input')

        # Test
        expected = ['Cupid', 'Himself', '1234124124', '20']
        for i in range(len(expected)):
            # inputs[0] will be csrf token, so inputs will be offset by 1
            self.assertEqual(expected[i], inputs[i+1].get_attribute('value'))

    def test_manager(self):
        utils.auto_login(self.browser, 'manager@cupidcode.com', '#/manager/home/5')
        # auto_login implicitly tests that you successfully reach homepage, it would
        # crash otherwise, which is all manager needs


if __name__ == '__main__':
    utils.db_backup()
    unittest.main(verbosity=2)
    utils.db_restore()
