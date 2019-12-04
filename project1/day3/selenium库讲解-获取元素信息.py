#获取属性，文本 标签
from selenium import webdriver
from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
url= "https://www.zhihu.com/explore"
browser.get(url)
# logo = browser.find_element_by_id('Button Button--primary Button--blue')
# print(logo)
# print(logo.get_attribute('class'))     #获取属性名称 get_attribute
# Button Button--primary Button--blue
input1 = browser.find_element_by_class_name('Button.Button--primary.Button--blue')
print(input1.text)         #获取文本值
print(input1.id)           #id
print(input1.location)     #位置
print(input1.tag_name)     #标签名
print(input1.size)  #大小

