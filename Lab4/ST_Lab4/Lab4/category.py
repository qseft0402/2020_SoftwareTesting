import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CategoryFeatures(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../venv/chromedriver')
        driver = self.driver
        driver.get("http://127.0.0.1:3000/")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_name("email").send_keys("demo@keystonejs.com")
        driver.find_element_by_name("password").send_keys("demo")
        driver.find_element_by_xpath("//button").click()
        time.sleep(1)

    def test_a_Create(self):
        print("Testing Create Category ............")
        driver = self.driver
        divList = driver.find_elements_by_class_name('dashboard-group__list-label')
        for div in divList:
            if div.text == "Categories":
                div.click()
                break
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        driver.find_element_by_name("name").send_keys("Test Create Category")
        driver.find_element_by_xpath("//form[1]").submit()
        time.sleep(1)
        driver.find_element_by_class_name('css-2960tt').click()
        driver.back()
        time.sleep(1)
        self.assertTrue(driver.find_element_by_link_text('Test Create Category') != None)
        print("Testing Create Category ............ OK")
        time.sleep(1)

    def test_b_Show(self):
        print("Testing Show Post Category ............")
        driver = self.driver
        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        driver.find_element_by_name("name").send_keys("Creat")
        driver.find_element_by_xpath("//form[1]").submit()
        time.sleep(1)
        inputList = driver.find_elements_by_tag_name('input')
        inputListReal = []
        [inputListReal.append(input) for input in inputList if input.is_displayed()]
        inputListReal[2].send_keys('Published')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        inputListReal[5].send_keys('Test Create Category')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        driver.find_element_by_class_name('css-2960tt').click()
        time.sleep(1)
        navbarList = driver.find_elements_by_class_name('primary-navbar__link')
        navbarList[len(navbarList) - 1].click()
        time.sleep(1)
        driver.find_element_by_tag_name('img').click()
        time.sleep(1)
        driver.find_element_by_link_text('Blog').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Test Create Category').click()
        time.sleep(1)
        self.assertTrue(driver.find_element_by_link_text('Creat') != None)
        print("Testing Show Post Category ............ OK")
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":

    unittest.main()
