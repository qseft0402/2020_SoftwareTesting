import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CommentsFeatures(unittest.TestCase):

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
        print("Testing Create Comment ............")
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
        driver.back()
        time.sleep(1)
        driver.find_element_by_link_text('Comments').click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(1)
        inputList = driver.find_elements_by_tag_name('input')
        inputListReal = []
        [inputListReal.append(input) for input in inputList if input.is_displayed()]
        if len(inputListReal) > 2:
            inputListReal.pop(0)
        inputListReal[0].send_keys('Demo User')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        inputListReal[1].send_keys('Creat')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        driver.find_element_by_xpath("//form[1]").submit()
        time.sleep(1)
        commentID = driver.find_element_by_tag_name('h2').text
        print('id:', commentID)
        driver.find_element_by_class_name('css-2960tt').click()
        driver.find_element_by_link_text('Comments').click()
        time.sleep(1)
        self.assertTrue(driver.find_element_by_partial_link_text(commentID) != None)
        self.assertTrue(driver.find_element_by_link_text('Demo User') != None)
        self.assertTrue(driver.find_element_by_partial_link_text('Creat') != None)
        print("Testing Create Comment ............ OK")
        time.sleep(1)

    def test_b_Edit(self):
        print("Testing Edit Comment ............")
        driver = self.driver
        divList = driver.find_elements_by_class_name('dashboard-group__list-label')
        for div in divList:
            if div.text == "Comments":
                div.click()
                break
        time.sleep(1)
        commentID = driver.find_element_by_class_name('ItemList__value--id').text
        driver.find_element_by_link_text(commentID).click()
        time.sleep(1)
        inputList = driver.find_elements_by_tag_name('input')
        inputListReal = []
        [inputListReal.append(input) for input in inputList if input.is_displayed()]
        #[print(idx, input.text) for idx, input in enumerate(inputListReal)]
        inputListReal[0].send_keys('Demo User')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        inputListReal[1].send_keys('Creat')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        inputListReal[2].send_keys('Draft')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        driver.switch_to.frame(0)
        driver.find_element_by_tag_name('body').send_keys('#Edit')
        driver.switch_to.default_content()
        driver.find_element_by_class_name('css-2960tt').click()
        selectValueList = driver.find_elements_by_class_name('Select-value-label')
        assert 'Demo User' in selectValueList[0].text
        assert 'Creat' in selectValueList[1].text
        assert 'Draft' in selectValueList[2].text
        print("Testing Edit Comment ............ OK")
        time.sleep(1)

    def test_c_Delete(self):
        print("Testing Delete Comment ............")
        driver = self.driver
        divList = driver.find_elements_by_class_name('dashboard-group__list-label')
        for div in divList:
            if div.text == "Comments":
                div.click()
                break
        time.sleep(1)
        commentID = driver.find_element_by_class_name('ItemList__value--id').text
        driver.find_element_by_link_text(commentID).click()
        print('id:', commentID)
        time.sleep(1)
        driver.find_element_by_class_name('css-1mj7u0z').click()
        driver.find_element_by_class_name('css-t4884').click()
        with self.assertRaises(NoSuchElementException):
            driver.find_element_by_link_text(commentID)
        print("Testing Delete Comment ............ OK")
        time.sleep(1)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":

    unittest.main()
