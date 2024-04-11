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

        self.wait = WebDriverWait(self.browser, timeout=5)
        self.browser.get('http://localhost:8000')
        self.browser.find_element(By.ID, 'login').click()
        self.addCleanup(lambda: (self.browser.quit(), utils.db_restore()))

    def claim_gigs(self):
        gigs = self.browser.find_elements(By.CLASS_NAME, 'inactive')
        for i in range(2):
            gig = self.browser.find_element(By.CLASS_NAME, 'inactive')
            gig.find_element(By.TAG_NAME, 'button').click()
            self.wait.until(lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == i+1)

    def navigate(self, link_text):
        self.browser.find_element(By.ID, 'navMenu').click()
        self.browser.find_element(By.LINK_TEXT, link_text).click()

    def test_gigs(self):
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')

        self.navigate('Gigs Available')
        self.claim_gigs()

        # Drop
        gigs = self.browser.find_elements(By.CLASS_NAME, 'active')
        self.assertEqual(len(gigs), 2)
        gigs[0].find_elements(By.TAG_NAME, 'button')[1].click()
        self.wait.until(lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 1)

        active = self.browser.find_elements(By.CLASS_NAME, 'active')
        self.assertEqual(len(active), 1)
        dropped = self.browser.find_elements(By.CLASS_NAME, 'inactive')
        self.assertEqual(len(dropped), 1)

    def test_gig_completion(self):
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        # Starting Balance
        self.navigate('Profile')
        self.assertEqual(self.browser.find_element(By.ID, 'balance').text, "$12.00")

        self.navigate('Gigs Available')
        self.claim_gigs()

        # Complete
        for i in range(2):
            active = self.browser.find_element(By.CLASS_NAME, 'active')
            active.find_element(By.TAG_NAME, 'button').click()
            self.wait.until(lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 1-i)

        self.navigate('Profile')
        self.assertEqual(self.browser.find_element(By.ID, 'balance').text, "$15.00")
        self.assertEqual(self.browser.find_element(By.ID, 'succesful').text, "6 gigs succesful of 22")


if __name__ == '__main__':
    unittest.main(verbosity=2)
