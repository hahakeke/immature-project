#元素查找，分为单元素查找和多元素查找
from selenium import webdriver
from selenium.webdriver.common.by import By   #引入通用查找

browser = webdriver.Chrome()
browser.get('https://www.taobao.com')
# print(browser.page_source)
#查找单一元素四种方式
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# # input_fourth = browser.find_element(By.ID,'q')    #通用单一查找
# print(input_first,input_second,input_third)
# browser.close()

#查找多个元素
lis = browser.find_elements_by_css_selector('.service-bd li')
lis1 = browser.find_elements_by_xpath('//*[@class="service-bd"]/li')
lis2 = browser.find_elements(By.CSS_SELECTOR,'.service-bd li')
print(lis,lis1,lis2)
print(len(lis),len(lis1),len(lis2))
browser.close()


