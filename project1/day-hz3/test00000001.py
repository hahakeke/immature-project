import requests
from lxml import etree

header = {"User-Agent":"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"}
url = "http://tieba.baidu.com/p/6341641910"
resp = requests.get(url,headers = header).content.decode()
with open("E://py/爬虫html保存/tieba1.html",'w',encoding='utf-8') as f:
    f.write(resp)
    f.close()
html = etree.HTML(resp)
title = html.xpath('//div[@class="core_title core_title_theme_bright"]/h1/text()')
data = str(title[0])
print(data)
# print(len(href_list))
# for i in href_list:
#     print(i)

