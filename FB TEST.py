from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):

#        self.driver = webdriver.Firefox(executable_path="/Users/markomasterl/Library/Selenium/WebDriver/firefox/geckodriver")
        self.driver = webdriver.Chrome(executable_path="/Users/markomasterl/Library/Selenium/WebDriver/chrome/chromedriver")
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()

    def test_login (self):

        driver = self.driver
        facebookUsername = ''
        facebookPassword = ''

        emailFieldID     = 'email'
        passFieldID      = 'pass'
#        loginButtonXpath = '//input[@value="loginbutton"]'
        loginButtonID    = 'loginbutton'
        fbLogoXpath      = '(//a[contains(@href, "logo")])[1]'

        emailFieldElement   = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement    = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
#        loginButtonElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        loginButtonElement  = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginButtonID))
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(fbLogoXpath))

        driver.quit()