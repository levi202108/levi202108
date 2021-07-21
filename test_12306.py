from selenium import  webdriver
import time 
driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("12306")
driver.find_element_by_id("su").click()
time.sleep(3)
dq=driver.current_window_handle
driver.find_element_by_partial_link_text("中国铁路").click()
ck=driver.window_handles
for i in ck:
    if i !=dq:
        driver.switch_to.window(i)
time.sleep(5)
driver.find_element_by_partial_link_text("车票").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='fromStationText']").click()
driver.find_element_by_xpath("//li[@title='合肥']").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@id='toStationText']").click()
driver.find_element_by_xpath("//li[@title='南京']").click()
time.sleep(4)
js='document.getElementById("train_date").removeAttribute("readonly")'
driver.execute_script(js)
driver.find_element_by_id("train_date").clear()
driver.find_element_by_id("train_date").send_keys("2021-05-27")
driver.find_element_by_xpath("//div[text()='27']").click()
time.sleep(3)
# js='document.getElementById("back_train_date").removeAttribute("readonly")'
# driver.execute_script(js)
# driver.find_element_by_id("back_train_date").clear()
# driver.find_element_by_id("back_train_date").send_keys("2021-05-28")
# driver.find_element_by_xpath("//div[text()='28']").click()
# time.sleep(3)
driver.find_element_by_xpath("//a[@id='search_one']").click()
time.sleep(3)
driver.get_screenshot_as_file(r"D:\软件测试\code\piao.png")
driver.quit()





