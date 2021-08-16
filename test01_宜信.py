from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
p=['13051667078','13103063559','17602163699','18511666968','13581685601','18335830533']
n=['张女士','王女士','王女士','刘先生','张女士','常先生']
class YiXin(unittest.TestCase):
    def setUp(self):
        self.web=webdriver.Chrome(executable_path='chromedriver.exe')
        self.web.get("http://www.baidu.com")
        self.web.maximize_window()
        self.web.find_element_by_id("kw").send_keys("宜信普惠")
        self.web.find_element_by_id("su").click()
        time.sleep(2)
        self.dq=self.web.current_window_handle
        self.web.find_element_by_xpath("//em[text()='宜信普惠']").click()
        time.sleep(2)
    def test_yixin(self):
        self.ck=self.web.window_handles
        for i in self.ck:
            if i !=self.dq:
                self.web.switch_to_window(i)
        self.web.find_element_by_id("name").send_keys(n[5])
        self.web.find_element_by_id('tel').send_keys(p[5])
        select1=self.web.find_element_by_id('num')
        jiekuan=Select(select1)
        jiekuan.select_by_value("100000")
        time.sleep(3)
        select2=self.web.find_element_by_id("usedFor")
        ytu=Select(select2)
        ytu.select_by_value("家居装修")
        self.web.find_element_by_id("city").send_keys("北京")
        time.sleep(3)
        js='window.scrollTo(0,-100)'
        self.web.execute_script(js)
        self.web.find_element_by_xpath("//button[text()='免费咨询']").click()
        time.sleep(5)
        self.web.find_element_by_xpath("//div[text()='确定']").click()
        time.sleep(4)
    def tearDown(self):
        self.web.quit()

if __name__=='__main__':
    unittest.main()






        