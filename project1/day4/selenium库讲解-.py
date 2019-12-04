#前进后退
# from selenium import webdriver
# import time
# browser = webdriver.Chrome()
# browser.get("https://www.baidu.com")
# time.sleep(5)
# browser.get("https://www.taobao.com")
# time.sleep(5)
# browser.get("https://www.zhihu.com/explore")
# time.sleep(5)
# browser.back()
# time.sleep(5)
# browser.forward()
# time.sleep(5)
# browser.close()


#cookies的获取
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.get("https://www.baidu.com")
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.baidu.com','value':'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

#选项卡管理(增加新窗口，打开新网页，切换页面)
# import time
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get("https://www.taobao.com")
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://www.zhihu.com')
# time.sleep(1)
# browser.quit()

#异常处理
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException

browser = webdriver.Chrome()
try:
    browser.get("https://www.baidu.com")
except TimeoutException:
    print('time out')
try:
    browser.find_element_by_id('hello')
except NoSuchElementException:
    print('NO ELEMENT')
finally:
    browser.close()