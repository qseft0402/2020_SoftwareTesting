import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

class EnquirieFeatures(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        driver = self.driver
        driver.get("http://127.0.0.1:3000/")
        time.sleep(1)

    def test_a_Create(self):
        print("Testing Create Enquirie ............")
        driver = self.driver
        driver.find_element_by_link_text('Contact').click()
        time.sleep(1)
        driver.find_element_by_name('name.full').send_keys('xue-shun li')
        driver.find_element_by_name('email').send_keys('islab@islab.com')
        driver.find_element_by_name('phone').send_keys('0900000000')
        Select(driver.find_element_by_name('enquiryType')).select_by_index(1)
        driver.find_element_by_name('message').send_keys('Hello World')
        driver.find_element_by_tag_name('form').submit()
        assert "Success!" in driver.find_element_by_tag_name('h1').text
        print("Testing Create Enquirie ............OK")
        time.sleep(1)

    def test_b_Create_Email_Invalid(self):
        print("Testing Create Email Invalid ............")
        driver = self.driver
        driver.find_element_by_link_text('Contact').click()
        time.sleep(1)
        driver.find_element_by_name('name.full').send_keys('xue-shun li')
        driver.find_element_by_name('email').send_keys('gg@123')
        driver.find_element_by_name('phone').send_keys('0900000000')
        Select(driver.find_element_by_name('enquiryType')).select_by_index(1)
        driver.find_element_by_name('message').send_keys('Hello World')
        driver.find_element_by_tag_name('form').submit()
        assert "Sorry, an error occurred loading the page (500)" in driver.find_element_by_tag_name('h1').text
        print("Testing Create Email Invalid ............ OK")
        time.sleep(1)

    def test_c_Show(self):
        print("Testing Delete Enquirie............ ")
        driver = self.driver
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_name("email").send_keys("demo@keystonejs.com")
        driver.find_element_by_name("password").send_keys("demo")
        driver.find_element_by_xpath("//button").click()
        time.sleep(1)
        driver.find_element_by_link_text("Enquiries").click()
        time.sleep(1)
        driver.find_element_by_link_text('xue-shun li').click()
        time.sleep(1)
        driver.find_element_by_class_name('css-1mj7u0z').click()
        driver.find_element_by_class_name('css-t4884').click()
        time.sleep(1)
        with self.assertRaises(NoSuchElementException):
            driver.find_element_by_link_text('islab@islab.com')
        print("Testing Delete Enquirie ............ OK")
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":

    unittest.main()
