from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
# options.add_argument("--proxy-server=http://183.164.238.153:9999")
# 无界面模式下默认不是全屏，所以需要设置一下分辨率
driver = webdriver.Chrome(options=options)
driver.set_window_size(1920, 1080)
driver.get('http://httpbin.org/ip')
print(driver.page_source)
