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

    def test_find(self):
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.browser.find_element(By.ID, 'find').click()

        gigs = self.browser.find_elements(By.CLASS_NAME, 'gig')
        self.assertEqual(len(gigs), 2)
        for gig in gigs:
            gig.find_elements(By.TAG_NAME, 'button')[0].click()
            help(gig)


if __name__ == '__main__':
    utils.db_backup()
    unittest.main(verbosity=2)
    utils.db_restore()
