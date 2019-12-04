from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

browser = webdriver.Chrome()
url = "https://login.taobao.com/member/login.jhtml?"
browser.get(url)
browser.execute_script("window.open()")
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get(url)
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get("http://www.baidu.com")


