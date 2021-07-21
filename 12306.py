from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.maximize_window()
driver.get(r"http://www.baidu.com")
time.sleep(2)
driver.find_element_by_id("kw").send_keys("12306")
driver.find_element_by_id("su").click()
time.sleep(3)
dq=driver.current_window_handle
driver.find_element_by_partial_link_text("中国铁路").click()
ck=driver.window_handles
for i in ck:
    if i != dq:
        driver.switch_to.window(i)
time.sleep(3)
driver.find_element_by_id("fromStationText").click()
driver.find_element_by_xpath("//li[text()='南京' and @title='南京']").click()
time.sleep(3)
driver.find_element_by_xpath("//li[text()='上海' and @title='上海']").click()
js='document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2021-05-18")
driver.find_element_by_xpath("//div[text()='18']").click()
time.sleep(3)
dq2=driver.current_window_handle
driver.find_element_by_id("search_one").click()
ck1=driver.window_handles
for j in ck1:
    if j != dq2:
        driver.switch_to.window(j)
driver.find_element_by_xpath("//a[@id='qd_closeDefaultWarningWindowDialog_id']").click()
time.sleep(4)
driver.get_screenshot_as_file(r"D:\软件测试\code\yupiao1.png")
time.sleep(3)
driver.quit()



