import unittest
from selenium import webdriver
import time
class Mytestcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def Test_baidu_search(self):
        driver = self.driver
        driver.find_element_by_id('kw').send_keys('陈雪爱')
        driver.find_element_by_class_name('btn self-btn bg s_btn').click()
        driver.find_element_by_xpath('//*[@id="9"]/h3').click()
    def tearDown(self):
        time.sleep(30)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

        


