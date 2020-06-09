from selenium import webdriver
# driver = webdriver.Chrome('chromedriver.exe')
import unittest
import time
from selenium.webdriver.common.keys import Keys

# driver.get('http://127.0.0.1:3000/')

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        # print("setUp")
        self.delayTime = 1
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

    def test_1_CreatUser(self):
        print('test_CreatUser......')
        self.driver.find_element_by_link_text('Users').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-we21er').click()
        self.driver.find_element_by_name('name.first').send_keys('ShengWen')
        self.driver.find_element_by_name('name.last').send_keys('Lu')
        self.driver.find_element_by_name('email').send_keys('108598007@ntut.edu.tw')
        self.driver.find_element_by_name('password').send_keys('00000000')
        self.driver.find_element_by_name('password_confirm').send_keys('00000000')
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/form/div[3]/button[1]').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('phone').send_keys('0912345678')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[1]/form/div[2]/div/div/button[1]').click()
        time.sleep(self.delayTime)
        self.driver.back()
        time.sleep(self.delayTime)

        try:
            self.driver.find_element_by_link_text('108598007@ntut.edu.tw')
            self.assertTrue(True)
            print('test_CreatUser......ok')
        except:
            self.assertTrue(False)
            print('test_CreatUser......fault')
        time.sleep(self.delayTime)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()