#等待（隐式等待，显式等待）
#隐式等待：当使用了隐式等待执行测试的时候，如果webdriver没在DOM中找到元素，将继续等待，超出设定时间后择抛出找不到元素的异常，换句话说，当查找元素或者元素并没有立即出现的时候，隐式等待将等待一段时间后再查找DOM，默认的时间是0。
#1.隐式等待
# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.implicitly_wait(10)
# browser.get("https://www.zhihu.com/explore")
# input1 = browser.find_element_by_class_name('Button.AppHeader-login.Button--blue')
# print(input1)

#2.显式等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
wait = WebDriverWait(browser,10)       #显示等待10秒
input1 = wait.until(EC.presence_of_element_located((By.ID,'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.btn-search')))
print(input1,button)