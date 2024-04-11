import sys
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import utils


class CupidTestCases(unittest.TestCase):

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

    def test_gigs(self):
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.browser.find_element(By.ID, 'find').click()

        # Claim
        gigs = self.browser.find_elements(By.CLASS_NAME, 'inactive')
        wait = WebDriverWait(self.browser, timeout=8)
        for i in range(2):
            gigs = self.browser.find_elements(By.CLASS_NAME, 'inactive')
            gigs[0].find_elements(By.TAG_NAME, 'button')[0].click()
        wait.until(lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 2)

        # Drop
        gigs = self.browser.find_elements(By.CLASS_NAME, 'active')
        self.assertEqual(len(gigs), 2)
        gigs[0].find_elements(By.TAG_NAME, 'button')[1].click()
        wait.until(lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 1)
        active = self.browser.find_elements(By.CLASS_NAME, 'active')
        self.assertEqual(len(active), 1)
        dropped = self.browser.find_elements(By.CLASS_NAME, 'inactive')
        self.assertEqual(len(dropped), 1)

        # Complete
        active[0].find_elements(By.TAG_NAME, 'button')[0].click()
        wait.until(lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 0)
        active = self.browser.find_elements(By.CLASS_NAME, 'active')
        self.assertEqual(len(active), 0)
        dropped = self.browser.find_elements(By.CLASS_NAME, 'inactive')
        self.assertEqual(len(dropped), 1)


if __name__ == '__main__':
    utils.db_restore()
    unittest.main(verbosity=2)
    utils.db_restore()
