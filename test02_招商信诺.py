import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
p=['1305****078','1310****559','176****3699','18511****68','1358****601','18****30533']
n=['张女士','王女士','王女士','刘先生','张女士','常先生']
class ZhaoShang(unittest.TestCase):
    def setUp(self):
        self.web=webdriver.Chrome(executable_path='chromedriver.exe')
        self.web.get("https://www.cignacmb.com/campaign/newdd06/?utm_source=baidu&utm_campaign=ROPDD&utm_adgroup=%E9%80%9A%E7%94%A8%E8%AF%8D&utm_term=%E4%BF%9D%E9%99%A9%E6%B5%8B%E8%AF%95&utm_medium=search-cpc&utm_channel=baidu-%E6%8B%9B%E5%95%86%E4%BF%A1%E8%AF%BA%E9%87%8D%E7%96%BE01-A20KA01380&iq_id=ze000111&cc=4GC1CMBDPCSEMYHD7&utm_keyword=203130639835&bd_vid=10704283505082714301")
        self.web.maximize_window()
        time.sleep(3)
    def test_baoxian(self):
        js='window.scrollTo(0,400)'
        self.web.execute_script(js)
        self.web.find_element_by_id("age").send_keys("37")
        time.sleep(3)
        self.web.find_element_by_xpath("//span[text()='男']").click()
        time.sleep(3)
        self.web.find_element_by_xpath('//li[text()="20-40万"]').click()
        time.sleep(3)
        self.web.find_element_by_xpath("//input[@id='name']").send_keys(n[5])
        self.web.find_element_by_xpath("//input[@id='mobile']").send_keys(p[5])
        time.sleep(3)
        self.web.find_element_by_xpath("//button[@id='submit_form']").click()
        time.sleep(3)
    def tearDown(self):
        self.web.quit()

if __name__=="__main__":
    unittest.main()    

        
