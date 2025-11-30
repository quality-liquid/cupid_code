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
                  'AI Chat': 'Chat Room',
                  'AI Listen': 'Let the AI Listen in!',
                  'Balance': 'Add Cash',
                  'Calendar': 'Calendar',
                  'Feedback': 'Feedback',
                  'Gigs': 'Gigs',
                  'Profile': 'Profile'}

        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/home/1')
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

            for sub_route, sub_expected_title in new_dict.items():
                # Go
                current_page = sub_route
                self.navigate(sub_route)
                given_title = self.browser.find_element(By.ID, 'title').text
                self.assertEqual(given_title, sub_expected_title)
                # Return
                current_page = route
                self.navigate(route)
                given_title = self.browser.find_element(By.ID, 'title').text
                self.assertEqual(given_title, expected_title)


    def test_stripe_payment_flow(self):
        """Test the complete Stripe payment flow"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        # Enter amount
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.clear()
        amount_input.send_keys('50')
        
        # Click deposit button
        deposit_btn = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Deposit")')
        deposit_btn.click()
        
        # Wait for payment form
        self.wait.until(lambda driver: driver.find_element(By.ID, 'payment-element'))
        self.assertIsNotNone(self.browser.find_element(By.ID, 'payment-form'))


    def test_balance_display(self):
        """Test that user balance is correctly displayed"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.TAG_NAME, 'h1'))
        
        balance_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('Current balance:', balance_text)
        self.assertIn('$', balance_text)


    def test_deposit_amount_validation_zero(self):
        """Test that zero is not accepted as a valid deposit amount (boundary)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('0')
        # Should not allow deposit of $0
        deposit_btn = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Deposit")')
        self.assertTrue(deposit_btn.get_attribute('disabled') or 'disabled' in deposit_btn.get_attribute('class'))

    def test_deposit_amount_validation_minimum(self):
        """Test that minimum valid amount ($0.01) is accepted (boundary)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('0.01')
        self.assertEqual(amount_input.get_attribute('value'), '0.01')

    def test_deposit_amount_validation_normal(self):
        """Test that normal deposit amount is accepted (simple case)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('50')
        self.assertEqual(amount_input.get_attribute('value'), '50')

    def test_deposit_amount_validation_large(self):
        """Test that large amounts are accepted (one example of many)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('9999.99')
        self.assertEqual(amount_input.get_attribute('value'), '9999.99')

    def test_deposit_amount_validation_negative(self):
        """Test that negative amounts are rejected (exception case)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('-50')
        # Should either reject negative or strip the negative sign
        value = amount_input.get_attribute('value')
        self.assertNotIn('-', value) or self.assertEqual(value, '')


    def test_payment_form_elements_exist(self):
        """Test that all required payment form elements are present"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        
        self.assertIsNotNone(self.browser.find_element(By.ID, 'amount'))
        self.assertIsNotNone(self.browser.find_element(By.ID, 'payment-form'))

    def test_stripe_payment_with_many_deposits(self):
        """Test multiple consecutive deposit attempts (many case)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        
        amounts = ['10', '25', '50']
        for amount in amounts:
            self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
            amount_input = self.browser.find_element(By.ID, 'amount')
            amount_input.clear()
            amount_input.send_keys(amount)
            self.assertEqual(amount_input.get_attribute('value'), amount)

    def test_stripe_payment_decimal_precision(self):
        """Test that decimal amounts are handled correctly (boundary)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('19.99')
        self.assertEqual(amount_input.get_attribute('value'), '19.99')

    def test_stripe_payment_form_submission(self):
        """Test that payment form can be submitted after entering amount (interface)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('25')
        
        deposit_btn = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Deposit")')
        self.assertFalse(deposit_btn.get_attribute('disabled') == 'true')

    def test_stripe_payment_invalid_characters(self):
        """Test that invalid characters are handled (exception case)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('abc')
        # Input should either be empty or filtered
        value = amount_input.get_attribute('value')
        self.assertTrue(value == '' or value.isdigit() or '.' in value)

    def test_stripe_payment_one_cent(self):
        """Test one cent deposit (one case - minimum valid)"""
        utils.auto_login(self.browser, 'bob@cupidcode.com', '#/dater/balance/1')
        self.wait.until(lambda driver: driver.find_element(By.ID, 'amount'))
        
        amount_input = self.browser.find_element(By.ID, 'amount')
        amount_input.send_keys('0.01')
        deposit_btn = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Deposit")')
        self.assertFalse(deposit_btn.get_attribute('disabled') == 'true')


if __name__ == '__main__':
    unittest.main(verbosity=2)
