from random import randint
from selenium import webdriver
import time 
driver=webdriver.Chrome(executable_path="chromedriver")
driver.get('http://www.baidu.com')
time.sleep(2)
driver.find_element_by_id('kw').send_keys('你好')
driver.find_element_by_id('su').click()
time.sleep(2)
driver.close()
