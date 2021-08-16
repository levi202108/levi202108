from selenium import webdriver
import time 
import unittest
n=['张女士','王女士','王女士','刘先生','张女士','常先生']
p=['13051667078','13103063559','17602163699','18511666968','13581685601','18335830533']
class Pingan(unittest.TestCase):
    def setUp(self):
        self.web=webdriver.Chrome(executable_path='chromedriver.exe')
        self.web.maximize_window()
        self.web.get("http://e.pingan.com/pa18shoplife/mobile/ydgw/index.html?WT.mc_id=mobi02-ydgw-sy-gw")
        time.sleep(2)
    def test_pingan(self):
        self.dq=self.web.current_window_handle
        self.web.find_element_by_xpath("//p[text()='健康保障']").click()
        self.ck=self.web.window_handles
        for i in self.ck:
            if i !=self.dq:
                self.web.switch_to_window(i)
        js='window.scrollTo(0,1000)'
        self.web.execute_script(js)
        self.dq1=self.web.current_window_handle
        self.web.find_element_by_xpath("//h3[text()='福运安康']").click()
        self.ck1=self.web.window_handles
        for j in self.ck1:
            if j !=self.dq1:
                self.web.switch_to_window(j)
        js='window.scrollTo(0,500)'
        self.web.execute_script(js)
        time.sleep(3)
        self.web.find_element_by_xpath("//input[@id='insurer_name']").send_keys(n[1])
        self.web.find_element_by_xpath("//span[@class='radio' and text()='女士']").click()
        time.sleep(3)
        js='window.scrollTo(0,200)'
        self.web.execute_script(js)
        self.web.find_element_by_xpath("//span[text()='25-35岁']").click()
        self.web.find_element_by_xpath("//span[text()='30万']").click()
        time.sleep(3)
        self.web.find_element_by_xpath("//input[@type='tel' and @name='insurerDTO.mobile']").send_keys(p[1])
        self.web.find_element_by_xpath("//p[text()='立即测算']").click()
        time.sleep(5)
    def tearDown(self):
        time.sleep(3)
        self.web.quit()

if __name__== '__main__':
    unittest.main()







        
        




