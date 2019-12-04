from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
url = "https://login.taobao.com/member/login.jhtml?"
browser.get(url)
print(browser.get_cookies())
browser.add_cookie({'name':'foo','value':'dad1'})    #cookie当前不能随意添加，至少该网址不能，模仿原有的cookie值，以字典形式添加
print(browser.get_cookies())
browser.delete_all_cookies()
print(browser.get_cookies())
browser.close()

# browser.find_element_by_class_name("forget-pwd J_Quick2Static").click()



