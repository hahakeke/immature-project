import os
from hashlib import md5
import pymongo
import requests,random,re
from urllib import parse
from bs4 import BeautifulSoup
from lxml import etree
from requests import RequestException
from day6.tiebaUpdate.tiebaconfig import *
from multiprocessing import Pool


client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
list1 = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
         "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
         "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE"]
Agent = random.choice(list1)
headers = {'User-Agent':Agent}


def get_page_index(offest,kw):
    data = {'kw':kw,
            'pn':offest}
    url = "http://tieba.baidu.com/f?" + parse.urlencode(data)
    resp = requests.get(url,headers=headers)
    return resp.text
def parse_page_index(html):
    pat = re.compile('<div class="threadlist_title pull_left j_th_tit ">\s+<a rel="noreferrer" href="(.*?)" title=',re.S)
    hrefs = re.findall(pat,html)
    for href in hrefs:
        link = "http://tieba.baidu.com" + href
        yield link
#访问详细页并获取title，图片链接
def get_detail_page(link):
    html = requests.get(link,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    title = soup.select(".core_title_txt")[0].get_text()
    html1 = etree.HTML(html)
    img_adress = html1.xpath('//div[@style="display:;"]/img[@class = "BDE_Image"]/@src')
    for adress in img_adress:
        download_img(adress)
    return {'title':title,
            'url':link,
            'img_adress':img_adress}

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到mongoDB成功',result)
        return True
    return False

def download_img(url):
    print('正在下载' + url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_images(response.content)
        return None
    except RequestException:
        print("请求图片页出错！")
        return None

def save_images(content):
    file_path = '{0}/{1}.{2}'.format('E:\py\爬虫二轮学习\IU\\',md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()

def main(offset):
    html = get_page_index(offset,KEYWORD)
    for link in parse_page_index(html):
        result = get_detail_page(link)
        if result:
            save_to_mongo(result)

if __name__ == '__main__':
    # for i in range(2):
    #      main(i*50)
    groups = [x*50 for x in range(GROUP_START,GROUP_END + 1)]
    pool = Pool()
    pool.map(main,groups)