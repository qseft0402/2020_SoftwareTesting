import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class PostFeatures(unittest.TestCase):

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
        print("Testing Create Post ............")
        driver = self.driver
        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        driver.find_element_by_name("name").send_keys("Li-xues-hun")
        driver.find_element_by_xpath("//form[1]").submit()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        assert 'Li-xues-hun' in driver.find_element_by_link_text('Li-xues-hun').text
        print("Testing Create Post ............ OK")
        time.sleep(1)

    def test_b_Edit(self):
        print("Testing Edit Post ............")
        driver = self.driver
        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)
        driver.find_element_by_link_text('Li-xues-hun').click()
        time.sleep(1)
        driver.find_element_by_name('name').clear()
        driver.find_element_by_name('name').send_keys('Li-xues-hun #Edit')
        inputList = driver.find_elements_by_tag_name('input')
        inputListReal = []
        [inputListReal.append(input) for input in inputList if input.is_displayed()]
        #[print(idx, input.get_attribute('value')) for idx, input in enumerate(inputListReal)]
        inputListReal[2].send_keys('Published')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        inputListReal[3].send_keys('Demo User')
        time.sleep(1)
        driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(1)
        inputListReal[4].send_keys(Keys.CONTROL,'a')
        inputListReal[4].send_keys(Keys.BACK_SPACE)
        inputListReal[4].send_keys('2019-05-16')
        driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_UP)
        iframeList = driver.find_elements_by_tag_name('iframe')
        [[iframe.send_keys(Keys.CONTROL,'a'), iframe.send_keys(Keys.BACK_SPACE), iframe.send_keys('#Edit')] for iframe in iframeList]
        # inputListReal[5].send_keys('normal')
        # driver.find_element_by_class_name('Select-menu-outer').click()
        driver.find_element_by_class_name('css-2960tt').click()
        time.sleep(1)
        assert 'Li-xues-hun #Edit' in driver.find_element_by_name('name').get_attribute('value')
        selectValueList = driver.find_elements_by_class_name('Select-value-label')
        #[print(idx, label.text) for idx, label in enumerate(selectValueList)]
        assert 'Published' in selectValueList[0].text
        assert 'Demo User' in selectValueList[1].text
        assert '2019-05-16' in inputListReal[4].get_attribute('value')
        driver.switch_to.frame(0)
        assert '#Edit' in driver.find_element_by_tag_name('body').text
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
        assert '#Edit' in driver.find_element_by_tag_name('body').text
        #print('Content Brief: ', driver.find_element_by_tag_name('body').text)
        #assert '#Edit' in driver.find_element_by_name('content.extended').text
        print("Testing Edit Post ............ OK")
        time.sleep(1)

    def test_c_Edit_Date_Invalid(self):
        print("Testing Edit Date Invalid ............")
        driver = self.driver
        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)
        driver.find_element_by_link_text('Li-xues-hun #Edit').click()
        time.sleep(1)
        inputList = driver.find_elements_by_tag_name('input')
        inputListReal = []
        [inputListReal.append(input) for input in inputList if input.is_displayed()]
        inputListReal[4].send_keys(Keys.CONTROL,'a')
        inputListReal[4].send_keys(Keys.BACK_SPACE)
        inputListReal[4].send_keys('abc')
        driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_DOWN)
        driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_UP)
        driver.find_element_by_class_name('css-2960tt').click()
        time.sleep(1)
        self.assertTrue(driver.find_element_by_class_name('css-1nqppvz') != None)
        print("Testing Edit Date Invalid ............ OK")
        time.sleep(1)

    def test_d_Delete(self):
        print("Testing Delete Post ............")
        driver = self.driver
        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)
        driver.find_element_by_link_text('Li-xues-hun #Edit').click()
        time.sleep(1)
        driver.find_element_by_class_name('css-1mj7u0z').click()
        driver.find_element_by_class_name('css-t4884').click()
        with self.assertRaises(NoSuchElementException):
            driver.find_element_by_link_text('Li-xues-hun #Edit')
        print("Testing Delete Post ............ OK")
        time.sleep(1)

    def test_d_Search(self):
        print("Testing Search Post............")
        driver = self.driver
        driver.find_element_by_link_text("Posts").click()
        time.sleep(1)
        try:
            driver.find_element_by_class_name('css-we21er').click()
        except:
            driver.find_element_by_class_name('css-h629qq').click()
        driver.find_element_by_name("name").send_keys("Li-xues-hun")
        driver.find_element_by_xpath("//form[1]").submit()
        time.sleep(1)
        driver.back()
        time.sleep(1)
        driver.find_element_by_tag_name('input').send_keys('this-post-was-created-by-selenium')
        self.assertTrue(len(driver.find_elements_by_link_text('Li-xues-hun')) > 0)
        print("Testing Search Post ............ OK")
        time.sleep(1)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
