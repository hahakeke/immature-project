import re,random
import requests
from lxml import etree
from requests.exceptions import RequestException
list1 = ["Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
         "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0",
         "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE"]
Agent = random.choice(list1)
headers = {'User-Agent':Agent}
proxies_list = []
def proxies_spider():
    resp = requests.get('https://www.xicidaili.com/nn/',headers=headers)
    print('正在获取代理IP，请稍后......')
    response = resp.content.decode()
    html1 = etree.HTML(response)
    ip_list = html1.xpath('//table[@id="ip_list"]/tr/td[6][contains(text(),"HTTPS")]/../td[2]/text()')
    port_list = html1.xpath('//table[@id="ip_list"]/tr/td[6][contains(text(),"HTTPS")]/../td[3]/text()')
    for i in range(len(ip_list)):
        ip_adress = ip_list[i] + ":" + port_list[i]
        yield ip_adress

def test_proxies(ip):
    try:
        proxy = {"https":ip}
        response = requests.get('http://httpbin.org/ip',proxies=proxy,headers=headers)
        if response.status_code==200:
            print(response.text)
            yield proxy
        else:
            return None
    except Exception as f:
        print(f)




def main():
    ip_adress = proxies_spider()
    for ip in ip_adress:
        useable_ip = test_proxies(ip)
        for i in useable_ip:
            print(i)



if __name__=='__main__':
    main()