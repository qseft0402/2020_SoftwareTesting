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

    def test_1_CreatPost(self):
        print('test_CreatPost......')
        self.driver.find_element_by_link_text('Posts').click() #click creat btn
        time.sleep(self.delayTime)
        try:
            self.driver.find_element_by_class_name('css-we21er').click()
        except:
            self.driver.find_element_by_class_name('css-h629qq').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').send_keys('test1 post') #fill text
        time.sleep(self.delayTime)
        # time.sleep(60)

        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/form/div[3]/button[1]').click() #creat btn
        # time.sleep(60)
        time.sleep(self.delayTime)

        self.driver.find_element_by_class_name('css-2960tt').click() #save btn
        time.sleep(self.delayTime)

        self.driver.back()
        try:
            assert 'test1 post' in self.driver.find_element_by_link_text('test1 post').text
            print('test_CreatPost......ok')
        except:
            print('test_CreatPost......fault')

    def test_2_EditPpst(self):
        print('test_post_editTitle......')
        self.driver.find_element_by_link_text('Posts').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text('test1 post').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').clear()
        time.sleep(self.delayTime)
        self.driver.find_element_by_name('name').send_keys('test1 post edited')  # set title
        time.sleep(self.delayTime)

        inputList = self.driver.find_elements_by_tag_name('input')
        inputListReal = []

        for input in inputList:
            if input.is_displayed():
                inputListReal.append(input)
        self.inputL=inputListReal
        inputListReal[2].send_keys('Archived')
        time.sleep(self.delayTime)

        self.driver.find_element_by_class_name('Select-menu-outer').click()

        time.sleep(self.delayTime)
        inputListReal[3].send_keys('Demo User')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('Select-menu-outer').click()
        time.sleep(self.delayTime)
        inputListReal[4].send_keys(Keys.CONTROL, 'a')
        inputListReal[4].send_keys(Keys.BACK_SPACE)
        inputListReal[4].send_keys('2020-06-10')
        time.sleep(self.delayTime)

        self.driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_class_name('css-2960tt').send_keys(Keys.ARROW_UP)
        time.sleep(self.delayTime)

        iframeList = self.driver.find_elements_by_tag_name('iframe')
        for iframe in iframeList:
            time.sleep(self.delayTime)
            iframe.send_keys(Keys.CONTROL,'a')
            time.sleep(self.delayTime)
            iframe.send_keys('this is iframe test edit')
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()  # click Save btn
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-2960tt').click()  # click Save btn
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element_by_link_text('test1 post edited').click()
        try:
            assert 'test1 post edited' in self.driver.find_element_by_name('name').get_attribute('value')
            print('test_post_editTitle......ok')
        except:
            print('test_post_editTitle......fault')

        selectList = self.driver.find_elements_by_class_name('Select-value-label')


        print('test_post_editState......')
        try:
            assert 'Archived' in selectList[0].text
            print('test_post_editState......ok')
        except:
            print('test_post_editState......fault')

        print('test_post_editAuthor......')
        try:
            assert 'Demo User' in selectList[1].text
            print('test_post_editAuthor......ok')
        except:
            print('test_post_editAuthor......fault')
        date=self.driver.find_element_by_tag_name('input')

        print('test_post_editDate......')

        try:
            assert '2020-06-10' in self.driver.find_element_by_name('publishedDate').get_attribute('value')
            print('test_post_editDate......ok')
        except:
            print('test_post_editDate......fault')

        print('test_post_editIframe1......')
        self.driver.switch_to.frame(0)
        try:
            assert 'this is iframe test edit' in self.driver.find_element_by_tag_name('body').text
            print('test_post_editiframe......ok')
        except:
            print('test_post_editiframe......fault')
        self.driver.switch_to.default_content()

        print('test_post_editIframe2......')
        self.driver.switch_to.frame(1)
        try:
            assert 'this is iframe test edit' in self.driver.find_element_by_tag_name('body').text
            print('test_post_editiframe......ok')
        except:
            print('test_post_editiframe......fault')


    def test_3_SearchPost(self):
        print('test_SearchPost......')

        self.driver.find_element_by_link_text('Posts').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/main/div/div/div[1]/div[1]/div[1]/div/input').send_keys('test1') #select search btn

        try:
            self.assertTrue(len(self.driver.find_elements_by_link_text('test1 post edited')) > 0)
            print('test_SearchPost......ok')
        except:
            print('test_SearchPost......fault')

        time.sleep(self.delayTime)
    def test_4_DeletePost(self):
        print('test_DeletePost......')
        self.driver.find_element_by_link_text('Posts').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_link_text('test1 post edited').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-1mj7u0z').click()
        time.sleep(self.delayTime)
        self.driver.find_element_by_class_name('css-t4884').click()
        try:
            self.assertTrue(len(self.driver.find_elements_by_link_text('test1 post edited')) == 0)
            print('test_DeletePost......ok')
        except:
            print('test_DeletePost......fault')
    def tearDown(self):
        # print("tearDown")
        time.sleep(3)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()






