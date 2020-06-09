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

    def test_1_CreatCategory(self):
        print('test_Category_CreateCategory......')
        time.sleep(self.delayTime)

        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[3]/span/a[1]/div[1]').click()
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_class_name('css-we21er').click()
        except:
            self.driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-foh633').send_keys('Test1 Category')
        time.sleep(self.delayTime)
        # try:
        #     self.driver.find_element_by_class_name('css-we21er').click()
        # except:
        #     self.driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]').click()
        except:
            self.driver.find_element_by_class_name('css-we21er').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-dmf4a8').click()
        time.sleep(self.delayTime)

        try:
            self.assertTrue(self.driver.find_element_by_link_text('Test1 Category') != None)
            print('test_CreatCategory......ok')
        except:
            print('test_CreatCategory......fault')

        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text('Posts').click()
        time.sleep(self.delayTime)


    def test_2_CreatPost(self):
        print('test_CreatPost......')
        time.sleep(self.delayTime)

        self.driver.find_element_by_link_text('Posts').click()  # click creat btn
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_class_name('css-we21er').click()
        except:
            self.driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').send_keys('test1 post')  # fill text
        time.sleep(self.delayTime)
        # time.sleep(60)

        try:
            self.driver.find_element_by_class_name('css-h629qq').click()
        except:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]').click()  # creat btn

        # time.sleep(60)
        time.sleep(self.delayTime)
        inputList=self.driver.find_elements_by_tag_name('input')
        inputListReal=[]
        for e in inputList:
            if e.is_displayed():
                inputListReal.append(e)
        time.sleep(self.delayTime)
        inputListReal[2].send_keys('Published')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(self.delayTime)
        inputListReal[3].send_keys('Demo User')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(self.delayTime)
        inputListReal[5].send_keys('Test1 Category')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()  # save btn
        time.sleep(self.delayTime)

        self.driver.back()
        try:
            assert 'test1 post' in self.driver.find_element_by_link_text('test1 post').text
            print('test_CreatPost......ok')
        except:
            print('test_CreatPost......fault')

    def test_3_ShowCategoriesOnBlog(self):
        print('test_ShowCategoriesOnBlog......')
        time.sleep(self.delayTime)
        menu=self.driver.find_elements_by_class_name('primary-navbar__link')
        menu[-2].click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text('Blog').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_partial_link_text('Test1 Category').click()
        time.sleep(self.delayTime)
        try:
            self.assertTrue(self.driver.find_element_by_link_text('test1 post') != None)
            print('test_ShowCategoriesOnBlog......ok')
        except:
            print('test_ShowCategoriesOnBlog......fault')
        time.sleep(self.delayTime)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()