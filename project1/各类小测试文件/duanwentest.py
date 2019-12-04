import requests
from lxml import etree
url = 'https://www.duanwenxue.com/article/4884936.html'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
resp = requests.get(url,headers=headers).text

with open("C:\\duanwen.html",'w',encoding='utf-8') as f:
    f.write(resp)

html = etree.HTML(resp)
content = html.xpath('//div[contains(@class,"article-content")]/p/text()')
print(content)