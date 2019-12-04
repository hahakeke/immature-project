import json
import os
import pymongo
import re
import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from hashlib import md5
from day401.Config import *
from multiprocessing import Pool

client = pymongo.MongoClient(MONGO_URL,connect=False)
db = client[MONGO_DB]
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
           'cookie':'tt_webid=6748367675662550532; csrftoken=a51812c39bde0a03ffd03cdaa4bdc8e7; tt_webid=6748367675662550532; WEATHER_CITY=%E5%8C%97%E4%BA%AC; s_v_web_id=240d7b6b3465bcae70d05a8c4a0bdd14; __tasessionId=89odfdjsc1571276131940'}
def get_one_page(offset,keyword):
    data={
        'aid': 24,
        'app_name':'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
    }
    url = 'https://www.toutiao.com/api/search/content/?' + urlencode(data)
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求索引页出错！")
        return None
def parse_one_page(html):
    pattern = re.compile('"abstract":"".*?"article_url":"(.*?)","behot_time"',re.S)
    detail_lists = re.findall(pattern,html)
    for list in detail_lists:
        yield list
def get_page_detail(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        print("请求详情页出错！")
        return None

def parse_page_detail(html,url):
    soup = BeautifulSoup(html,'lxml')
    title = soup.select('title')[0].get_text()
    print(title)
    images_pattern = re.compile('gallery: JSON.parse\((.*?)\)',re.S)
    result = re.search(images_pattern,html)
    if result:
        data1 = json.loads(result.group(1))
        data = json.loads(data1)
        if data and 'sub_images' in data.keys():
            sub_images = data.get('sub_images')
            images = [item.get('url') for item in sub_images]
            for image in images:download_image(image)
            return {
                'title':title,
                'url':url,
                'images':images
            }
def download_image(url):
    print('正在下载'+url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            save_images(response.content)
        return None
    except RequestException:
        print("请求图片页出错！")
        return None
def save_images(content):
    file_path = '{0}/{1}.{2}'.format('E:\py\爬虫二轮学习\街拍\\',md5(content).hexdigest(),'jpg')
    if not os.path.exists(file_path):
        with open(file_path,'wb') as f:
            f.write(content)
            f.close()
def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('存储到mongoDB成功',result)
        return True
    return False

def main(offset):
    html = get_one_page(offset,KEYWORD)
    for url in parse_one_page(html):
        html = get_page_detail(url)
        if html:
            result = parse_page_detail(html,url)
            if result:
                save_to_mongo(result)

if __name__=='__main__':
    # for i in range(10):
    #     main(i*20)
    groups = [x*20 for x in range(GROUP_START,GROUP_END + 1)]
    pool = Pool()
    pool.map(main,groups)


