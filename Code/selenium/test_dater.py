import sys
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import utils


class DaterTestCases(unittest.TestCase):

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

    
    # nav testing
    def navigate(self, link_text):
        self.browser.find_element(By.ID, 'navMenu').click()
        self.browser.find_element(By.LINK_TEXT, link_text).click()

    def test_navigation(self):
        routes = {'Home': 'Home',
                  'Profile': 'Profile',
                  'Gigs Available': 'Gigs',
                  'Gigs Completed': 'Completed Gigs',
                  'Feedback': 'Feedback'}

        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        current_page = "Home"
        homeless_dict = {key: value for key, value in routes.items() if key != current_page}

        for route, expected_title in homeless_dict.items():
            if route == current_page:
                self.navigate("Home")
            current_page = route
            self.navigate(route)
            given_title = self.browser.find_element(By.ID, 'title').text
            self.assertEqual(given_title, expected_title)
            new_dict = {key: value for key, value in routes.items() if key != route}

            for sub_route, sub_expected_title in routes.items():
                current_page = sub_route
                self.navigate(sub_route)
                given_title = self.browser.find_element(By.ID, 'title').text
                self.assertEqual(given_title, sub_expected_title)




if __name__ == '__main__':
    unittest.main(verbosity=2)
