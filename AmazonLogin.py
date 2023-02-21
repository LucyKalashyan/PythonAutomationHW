import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class AmazonLoginTC(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    def test_login(self):
        loginFieldElement = self.driver.find_element(By.NAME, "email")
        loginFieldElement.send_keys("bobsmithamazon7@gmail.com")
        time.sleep(3)
        continueButton = self.driver.find_element(By.ID, "continue")
        continueButton.click()
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.send_keys("amazonpass")
        rememberMeButton = self.driver.find_element(By.NAME, "rememberMe")
        rememberMeButton.click()
        time.sleep(3)
        submitButton = self.driver.find_element(By.ID, "signInSubmit")
        submitButton.click()

        assert self.driver.title == "Amazon Sign-In"

    def tearDown(self):
        time.sleep(4)
        self.driver.close()
