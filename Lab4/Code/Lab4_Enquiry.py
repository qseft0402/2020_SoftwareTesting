from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
import unittest
import time
from selenium.webdriver.common.keys import Keys

# driver.get('http://127.0.0.1:3000/')

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # print("setUp")
        self.delayTime = 0.5
        self.driver = webdriver.Chrome('chromedriver.exe')
        # self.driver = webdriver.Chrome('/Users/awen/Desktop/ST-Lab4/chromedriver')
        # self.driver.fullscreen_window()
        self.driver.get('http://127.0.0.1:3000/')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[1]/div[2]/a').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('email').send_keys('demo@keystonejs.com')
        self.driver.find_element_by_name('password').send_keys('demo')
        self.driver.find_element_by_class_name('css-2960tt').click()
        time.sleep(self.delayTime)

    def test_1_CreatEnquiry(self):
        print('test_CreatEnquiry......')
        menu = self.driver.find_elements_by_class_name('primary-navbar__link')
        menu[-2].click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text('Contact').click()
        time.sleep(self.delayTime)
        inputList=self.driver.find_elements_by_tag_name('input')
        inputListReal=[]
        for e in inputList:
            if e.is_displayed():
                inputListReal.append(e)
        inputListReal[0].send_keys('Demo User')
        inputListReal[1].send_keys('demo@keystonejs.com')

        time.sleep(self.delayTime)
        selectList=self.driver.find_elements_by_tag_name('select')
        selectList[0].send_keys('Just leaving a message')
        time.sleep(self.delayTime)
        self.driver.find_element_by_tag_name('textarea').send_keys('This is a test to Enquiry')
        time.sleep(self.delayTime)
        btnList=self.driver.find_elements_by_tag_name('button')
        time.sleep(self.delayTime)
        btnList[1].click()
        time.sleep(self.delayTime)
        try:
            if self.driver.find_element_by_tag_name('h1').text == 'Success!':
                print('test_CreatEnquiry......ok')
        except:
            print('test_CreatEnquiry......fault')

        time.sleep(1)

    def test_2_DeleEnquiry(self):
        print('test_DeleEnquiry......')
        self.driver.find_element_by_link_text('Enquiries').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text('Demo User').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div/form/div[2]/div/div/button[3]').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-t4884').click()
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_link_text('test Enquirie')
            self.assertTrue(False)
            print('test_DeleEnquiry......fault')
        except:
            self.assertTrue(True)
            print('test_DeleEnquiry......ok')

        time.sleep(self.delayTime)
        time.sleep(self.delayTime)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()