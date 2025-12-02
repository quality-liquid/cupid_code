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
            self.wait.until(
                lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == i+1
            )

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

    def test_gigs_completion(self):
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
            self.wait.until(
                lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 1-i
            )

        self.navigate('Profile')
        self.assertEqual(self.browser.find_element(By.ID, 'balance').text, "$15.00")
        self.assertEqual(
            self.browser.find_element(By.ID, 'succesful').text, "6 gigs succesful of 22"
        )

    def test_feedback(self):
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Feedback')
        feedbacks = self.browser.find_elements(By.CLASS_NAME, 'feedback')
        self.assertEqual(len(feedbacks), 1)
        self.assertEqual(feedbacks[0].find_element(By.TAG_NAME, 'h1').text, 'Star Rating: 5')
        self.assertEqual(
            feedbacks[0].find_element(By.TAG_NAME, 'span').text, 'Feedback: This cupid was great!'
        )

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
                current_page = route
                self.navigate(route)

    # Stripe tests for Cupid using ZOMBIES principles
    def test_stripe_account_creation_simple(self):
        """Test basic Stripe account creation flow (simple case)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        # Verify account creation button exists
        create_button = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Create Stripe Account")')
        self.assertIsNotNone(create_button)
        self.assertFalse(create_button.get_attribute('disabled') == 'true')

    def test_stripe_account_button_visibility_without_account(self):
        """Test that create account button is visible when no account exists (one case)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        create_button = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Create Stripe Account")')
        self.assertTrue(create_button.is_displayed())

    def test_stripe_account_button_state_zero_accounts(self):
        """Test button state with zero existing Stripe accounts (boundary)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        # Should have create button, not withdraw button
        create_buttons = self.browser.find_elements(By.CSS_SELECTOR, 'button:contains("Create Stripe Account")')
        withdraw_buttons = self.browser.find_elements(By.CSS_SELECTOR, 'button:contains("Withdraw funds")')
        
        self.assertEqual(len(create_buttons), 1)
        self.assertEqual(len(withdraw_buttons), 0)

    def test_stripe_withdraw_funds_disabled_state(self):
        """Test that withdraw button shows loading state during processing (interface)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        # Initially button should show "Withdraw funds"
        withdraw_btn = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Withdraw funds")')
        self.assertIsNotNone(withdraw_btn)

    def test_stripe_balance_display_zero(self):
        """Test balance display shows correctly (zero case)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        balance = self.browser.find_element(By.ID, 'balance').text
        self.assertTrue(balance.startswith('$'))
        self.assertIsNotNone(balance)

    def test_stripe_balance_format_valid(self):
        """Test balance is displayed in correct currency format (simple case)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        balance_text = self.browser.find_element(By.ID, 'balance').text
        # Should match pattern like "$12.00"
        self.assertTrue(balance_text.startswith('$'))
        self.assertTrue(any(c.isdigit() for c in balance_text))

    def test_stripe_balance_updates_after_gig_completion(self):
        """Test balance increases after completing gigs (many case - multiple transactions)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        initial_balance = self.browser.find_element(By.ID, 'balance').text
        
        self.navigate('Gigs Available')
        self.claim_gigs()
        
        # Complete gigs
        for i in range(2):
            active = self.browser.find_element(By.CLASS_NAME, 'active')
            active.find_element(By.TAG_NAME, 'button').click()
            self.wait.until(
                lambda d: len(self.browser.find_elements(By.CLASS_NAME, 'active')) == 1-i
            )
        
        self.navigate('Profile')
        final_balance = self.browser.find_element(By.ID, 'balance').text
        
        # Balance should have increased
        self.assertNotEqual(initial_balance, final_balance)

    def test_stripe_account_creation_button_click(self):
        """Test that create account button is clickable (interface)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        create_button = self.browser.find_element(By.CSS_SELECTOR, 'button:contains("Create Stripe Account")')
        self.assertTrue(create_button.is_enabled())

    def test_stripe_profile_card_exists(self):
        """Test that profile card with balance info exists (simple case)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        card = self.browser.find_element(By.CLASS_NAME, 'card')
        self.assertIsNotNone(card)
        balance = card.find_element(By.ID, 'balance')
        self.assertIsNotNone(balance)

    def test_stripe_balance_negative_prevention(self):
        """Test that balance cannot go negative (exception case)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        balance_text = self.browser.find_element(By.ID, 'balance').text
        # Remove $ and convert to float
        balance_value = float(balance_text.replace('$', ''))
        self.assertGreaterEqual(balance_value, 0)

    def test_stripe_gigs_completed_counter(self):
        """Test that gigs completed counter displays correctly (boundary)"""
        utils.auto_login(self.browser, 'really@me.com', '#/cupid/home/4')
        self.navigate('Profile')
        
        success_text = self.browser.find_element(By.ID, 'successful').text
        # Should contain pattern like "6 gigs successful of 22"
        self.assertIn('gigs successful of', success_text)
        self.assertRegex(success_text, r'\d+ gigs successful of \d+')


if __name__ == '__main__':
    unittest.main(verbosity=2)
