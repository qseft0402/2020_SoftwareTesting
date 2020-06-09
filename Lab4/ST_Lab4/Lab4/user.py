import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class UserFeatures(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        driver = self.driver
        driver.get("http://127.0.0.1:3000/")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_name("email").send_keys("demo@keystonejs.com")
        driver.find_element_by_name("password").send_keys("demo")
        driver.find_element_by_xpath("//button").click()
        time.sleep(1)

    def test_a_Create(self):
        print("Testing Create User ............")
        driver = self.driver
        driver.find_element_by_link_text('Users').click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        driver.find_element_by_name('name.first').send_keys('xue-shun')
        driver.find_element_by_name('name.last').send_keys('lee')
        driver.find_element_by_name('email').send_keys('ddd@islab.com')
        driver.find_element_by_name('password').send_keys('enoqewofmoef')
        driver.find_element_by_name('password_confirm').send_keys('enoqewofmoef')
        driver.find_element_by_tag_name('form').submit()
        time.sleep(1)
        driver.find_element_by_name('phone').send_keys('0900000000')
        driver.find_element_by_class_name('css-2960tt').click()
        driver.back()
        time.sleep(1)
        self.assertTrue(driver.find_element_by_link_text('xue-shun lee') != None)
        print("Testing Create User ............ OK")
        time.sleep(1)

    def test_b_Create_Password_Invalid_Too_Short(self):
        print("Testing Password Invalid Too Short ............")
        driver = self.driver
        driver.find_element_by_link_text('Users').click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        driver.find_element_by_name('name.first').send_keys('first')
        driver.find_element_by_name('name.last').send_keys('last')
        driver.find_element_by_name('email').send_keys('abc@apple.com')
        driver.find_element_by_name('password').send_keys('123')
        driver.find_element_by_name('password_confirm').send_keys('123')
        driver.find_element_by_tag_name('form').submit()
        time.sleep(1)
        divList = driver.find_elements_by_tag_name('div')
        error = ""
        for div in divList:
            if div.text == "Password must be longer than 8 characters.":
                error = div.text
                break
        assert "Password must be longer than 8 characters." in error
        print("Testing Password Invalid Too Short ............ OK")
        time.sleep(1)

    def test_c_Create_Password_Invalid_Too_Simple(self):
        print("Testing Password Invalid Too Simple ............")
        driver = self.driver
        driver.find_element_by_link_text('Users').click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        driver.find_element_by_name('name.first').send_keys('Password')
        driver.find_element_by_name('name.last').send_keys('Too Simple')
        driver.find_element_by_name('email').send_keys('abc@apple.com')
        driver.find_element_by_name('password').send_keys('12345678')
        driver.find_element_by_name('password_confirm').send_keys('12345678')
        driver.find_element_by_tag_name('form').submit()
        time.sleep(1)
        divList = driver.find_elements_by_tag_name('div')
        error = ""
        for div in divList:
            if div.text == "Password must not be a common, frequently-used password.":
                error = div.text
                break
        assert "Password must not be a common, frequently-used password." in error
        print("Testing Password Invalid Too Simple ............ OK")
        time.sleep(1)

    def test_d_Create_Password_Invalid_Not_Match(self):
        print("Testing Password Invalid Not Match...")
        driver = self.driver
        driver.find_element_by_link_text('Users').click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        driver.find_element_by_name('name.first').send_keys('fitst')
        driver.find_element_by_name('name.last').send_keys('last')
        driver.find_element_by_name('email').send_keys('abc@apple.com')
        driver.find_element_by_name('password').send_keys('aqweojqweirogj')
        driver.find_element_by_name('password_confirm').send_keys('pnkeqwuiehne')
        driver.find_element_by_tag_name('form').submit()
        time.sleep(1)
        divList = driver.find_elements_by_tag_name('div')
        error = ""
        for div in divList:
            if div.text == "Passwords must match.":
                error = div.text
                break
        assert "Passwords must match." in error
        print("Testing Password Invalid Not Match ............ OK")
        time.sleep(1)

    def test_e_Create_Email_Invalid(self):
        print("Testing Email Invalid ............")
        driver = self.driver
        driver.find_element_by_link_text('Users').click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        driver.find_element_by_name('name.first').send_keys('Email')
        driver.find_element_by_name('name.last').send_keys('Invalid')
        driver.find_element_by_name('email').send_keys('123@123')
        driver.find_element_by_name('password').send_keys('pineapplePen')
        driver.find_element_by_name('password_confirm').send_keys('pineapplePen')
        driver.find_element_by_tag_name('form').submit()
        time.sleep(1)
        divList = driver.find_elements_by_tag_name('div')
        error = ""
        for div in divList:
            if div.text == "Email is invalid":
                error = div.text
                break
        assert "Email is invalid" in error
        print("Testing Email Invalid ............ OK")
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":

    unittest.main()
