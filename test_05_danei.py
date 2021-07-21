from selenium import webdriver
from time import sleep
import unittest
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
phone=['17602163699','18511666968','04318123712','13581685601']
class Danei(unittest.TestCase):
    def setUp(self) -> None:
        self.web=webdriver.Firefox()
        self.web.get("http://www.baidu.com")
        self.web.find_element_by_id("kw").send_keys("达内")
        self.web.find_element_by_id("su").click()
        sleep(3)
    def test_01(self):
        self.dq=self.web.current_window_handle
        self.web.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/div/div/div[1]/div/h2/a[1]").click()
        self.web.maximize_window()
        self.ck=self.web.window_handles
        for i in self.ck:
            if i !=self.ck:
                self.web.switch_to.window(i)
        sleep(6)
        self.web.maximize_window()
        self.web.switch_to.frame("iframe_company_mini")
        sleep(4)
        self.web.find_element_by_xpath("/html/body/div[2]/div/div/div[3]/div/div[5]/div[3]/div[1]/div[2]/div/div[3]/div/div[2]").click()
        sleep(5)
        random.shuffle(phone)
        k=random.choice(phone)
        self.web.find_element_by_class_name("inputArea").click()
        sleep(4)
        self.web.find_element_by_class_name("inputArea").send_keys(k)
        self.web.find_element_by_xpath("//a[@id='btnSend']").click()
        sleep(5)

    def tearDown(self) -> None:
        self.web.quit()

if __name__=="__main__":
    unittest.main()