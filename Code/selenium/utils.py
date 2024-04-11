import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def flagParse():
    chrome = False
    headless = False
    with open('options.conf', 'r') as options:
        for line in options:
            if 'headless' in line:
                headless = 'true' in line
            if 'chrome' in line:
                chrome = 'true' in line
    return chrome, headless


def auto_login(browser, email, url):
    # Navigate
    browser.find_element(By.ID, 'email').send_keys(email)
    browser.find_element(By.ID, 'password').send_keys('password')
    browser.find_element(By.ID, 'sign_in').click()

    # Wait until ready
    wait = WebDriverWait(browser, timeout=2)
    wait.until(lambda d: url in browser.current_url)


def db_restore():
    # print('restoring')
    shutil.copy('../server/db_backup.sqlite3', '../server/db.sqlite3')


if __name__ == '__main__':
    db_restore()
