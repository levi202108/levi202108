from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path=r"chromedriver.exe")
driver.maximize_window()
driver.get(r"http://www.baidu.com")
dq=driver.current_window_handle
driver.find_element_by_link_text("登录").click()
ck=driver.window_handles
for i in ck:
    if  i != dq:
        driver.switch_to.window(i)
time.sleep(3)
dq1=driver.current_window_handle
driver.find_element_by_xpath("//p[text()='用户名登录']").click()
ck1=driver.window_handles
for j in ck:
    if  j != dq:
        driver.switch_to.window(j)
time.sleep(3)
driver.find_element_by_name("userName").send_keys("baidu")
driver.find_element_by_name("password").send_keys("baidu123456")
driver.find_element_by_xpath("//input[@value='登录']").click()
time.sleep(3)
driver.quit()

