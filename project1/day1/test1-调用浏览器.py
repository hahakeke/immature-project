#以两种方式调用浏览器访问"http://www.baidu.com"

#使用Chrome浏览器/phantomjs
# from selenium import webdriver
# driver = webdriver.Chrome()
# # driver = webdriver.PhantomJS()
# driver.get("http://www.baidu.com")
# print(driver.page_source)

# from selenium.webdriver import Firefox
# from selenium.webdriver.firefox.options import Options
#
# def main():
#     options = Options()
#     options.add_argument('-headless')
#     driver = Firefox(executable_path='C:\Python37\geckodriver', options=options)
#     driver.get("http://www.baidu.com")
#     print(driver.page_source)
#     driver.close()
#
#
# if __name__ == '__main__':
#     main()


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.baidu.com")
print(driver.page_source)
driver.close()

