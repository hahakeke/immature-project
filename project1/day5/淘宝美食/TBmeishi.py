import re,time
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day5.淘宝美食.config import *
import pymongo
n = 0
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
driverOptions = webdriver.ChromeOptions()

driverOptions.add_argument(r"user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data")
browser = webdriver.Chrome("chromedriver",0,driverOptions)
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# browser.set_window_size(1400,900)
wait =WebDriverWait(browser, 10)
def search():
    print('正在搜索！')
    try:
        browser.get("http://www.taobao.com")
        #判断是否加载成功
        input1 = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
        input1.send_keys("美食")
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.total')))
        get_product()
        return total.text
    except TimeoutException:
        return search()
def next_page(page_number):
    print('正在跳转页面',page_number)
    time.sleep(10)
    try:
        input1 = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.input:nth-child(2)"))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'span.btn:nth-child(4)')))
        input1.clear()
        input1.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'span.num'),str(page_number)))
        get_product()
    except TimeoutException:
        next_page(page_number)
def get_product():
    global n
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .J_ItemPic.img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'shop':item.find('.shop').text(),
            'localtion':item.find('.location').text()
        }
        n += 1
        print(product,n)
        save_to_mongodb(product)
def save_to_mongodb(product):
    try:
        if db[MONGO_TABLE].insert(product):
            print("存储到MONGODB成功！",product)
    except Exception:
        print("存储到MONGODB失败！",product)


def main():
    total=search()
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2,total + 1):
        next_page(i)
    browser.close()

if __name__ =='__main__':
    main()
