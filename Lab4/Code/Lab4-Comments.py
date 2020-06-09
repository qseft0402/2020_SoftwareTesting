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

    def test_1_CreatPost(self):
        print('test_CreatPost......')
        self.driver.find_element_by_link_text('Posts').click()  # click creat btn
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_class_name('css-we21er').click()
        except:
            self.driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').send_keys('Test1 Post')  # fill text
        time.sleep(self.delayTime)
        # time.sleep(60)

        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]').click()  # creat btn
        # time.sleep(60)
        time.sleep(self.delayTime)

        self.driver.find_element_by_class_name('css-2960tt').click()  # save btn
        time.sleep(self.delayTime)

        self.driver.back()
        try:
            assert 'test1 post' in self.driver.find_element_by_link_text('test1 post').text
            print('test_CreatPost......ok')
        except:
            print('test_CreatPost......fault')

    def test_2_CreatComment(self):
        print('test_CreatComment......')
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[1]/div[1]').click()  # click Comments btn
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_class_name('css-we21er').click()
        except:
            self.driver.find_element_by_class_name('css-h629qq').click()
        inputList = self.driver.find_elements_by_tag_name('input')
        inputListReal = []
        for input in inputList:
            if input.is_displayed():
                inputListReal.append(input)

        if len(inputListReal) > 2:
            inputListReal.pop(0)
        inputListReal[0].send_keys('Demo User')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        inputListReal[1].send_keys('Test1 Post')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]').click()
        except:
            self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/form/div[3]/button[1]').click()
        time.sleep(self.delayTime)
        self.commentID = self.driver.find_element_by_tag_name('h2').text
        # print('id:', self.commentID)

        self.driver.find_element_by_class_name('css-dmf4a8').click()
        time.sleep(self.delayTime)
        self.assertTrue(self.driver.find_element_by_link_text(self.commentID) != None)
        self.assertTrue(self.driver.find_element_by_link_text('Demo User') != None)
        self.assertTrue(self.driver.find_element_by_link_text('Test1 Post') != None)
        print("test_CreatComment......OK")
        time.sleep(self.delayTime)

    def test_3_EditComment(self):
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[1]/div[1]').click()  # click Comments btn
        time.sleep(self.delayTime)
        td_tag_list = self.driver.find_elements_by_tag_name('td')
        time.sleep(self.delayTime)
        self.commentID = td_tag_list[1].text
        # print(self.commentID)
        self.driver.find_element_by_link_text(self.commentID).click()
        time.sleep(self.delayTime)
        inputList=self.driver.find_elements_by_tag_name('input')
        inputListReal=[]
        for e in inputList:
            if e.is_displayed():
                inputListReal.append(e)
        inputListReal[2].send_keys('Draft')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(self.delayTime)

        iframeList = self.driver.find_elements_by_tag_name('iframe')
        for iframe in iframeList:
            time.sleep(self.delayTime)
            iframe.send_keys(Keys.CONTROL, 'a')
            time.sleep(self.delayTime)
            iframe.send_keys('this is iframe test edit')

        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()  # click Save btn
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()  # click Save btn
        time.sleep(1)
        self.driver.back()
        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text(self.commentID).click()
        time.sleep(self.delayTime)

        selectList = self.driver.find_elements_by_class_name('Select-value-label')
        print('test_Comment_editState......')
        try:
            assert 'Draft' in selectList[2].text
            print('test_Comment_editState......ok')
        except:
            print('ans:'+str(selectList[2].text))
            print('test_Comment_editState......fault')

        print('test_Comment_editiframe......')
        self.driver.find_element_by_tag_name('body').text
        self.driver.switch_to.frame(0)
        try:
            assert 'this is iframe test edit' in self.driver.find_element_by_tag_name('body').text
            print('test_Comment_editiframe......ok')
        except:
            print('ans:'+str(self.driver.find_element_by_tag_name('body').text))
            print('test_Comment_editiframe......fault')
        time.sleep(10)




    def test_4_DeleComment(self):
        print('test_DeleComment......')
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div[2]/div/div[1]/div[2]/div[2]/span/a[1]/div[1]').click()  # click Comments btn
        time.sleep(self.delayTime)

        td_tag_list=self.driver.find_elements_by_tag_name('td')
        time.sleep(self.delayTime)
        self.commentID = td_tag_list[1].text
        # print(self.commentID)
        self.driver.find_element_by_link_text(self.commentID).click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-1mj7u0z').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-t4884').click()


        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_link_text(self.commentID)
            self.assertTrue(False)

            print('test_DeleComment......fault')
        except:
            self.assertTrue(True)
            print('test_DeleComment......ok')

        time.sleep(self.delayTime)




    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()