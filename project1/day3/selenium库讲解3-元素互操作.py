from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
input1 = browser.find_element_by_id('q')
input1.send_keys('iphone')
time.sleep(5)
input1.clear()
input1.send_keys('ipad')
button = browser.find_element_by_class_name('btn-search')
button.click()
time.sleep(5)
browser.close()