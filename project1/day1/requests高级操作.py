#1.文件上传
# import requests
# file = {'file':open('cookie.txt','rb')}
# response = requests.post("http://httpbin.org/post",files = file)
# print(response.text)

#2.获取cookie
# import requests
# response = requests.get("http://www.baidu.com")
# print(response.cookies)
# for key,value in response.cookies.items():
#     print(key + '=' + value)

#3.会话维持，模拟登陆
# import requests
# s = requests.Session()
# s.get("http://httpbin.org/cookies/set/number/123456789")
# response = s.get("http://httpbin.org/cookies")
# print(response.text)

#4.证书验证
# import requests
# from requests.packages import urllib3
# urllib3.disable_warnings()
# response = requests.get("https://www.12306.cn",verify = False)
# print(response.status_code)
# print(response.content.decode('utf-8'))

#5.代理IP设置
#1
# import requests
# proxies = {
#     "http":"http://127.0.0.1:9743",
#     "https":"https://127.0.0.1:9743",
# }      #代理IP未进行验证，仅作为案例
# response = requests.get("https://www.taobao.com",proxies = proxies)
# print(response.status_code)

#2
# import requests
# proxies = {
#     "http":"http://user:password@127.0.0.1:9743/",
# }      #代理IP未进行验证，仅作为案例
# response = requests.get("https://www.taobao.com",proxies = proxies)
# print(response.status_code)

#(3).socks 需安装socks，pip install request(socks)
# import requests
# proxies = {
#     "http":"socks5://127.0.0.1:9742/",
# }      #代理IP未进行验证，仅作为案例
# response = requests.get("https://www.taobao.com",proxies = proxies)
# print(response.status_code)

#6.超时设置。在requests.get(url,timeout = t) t为需要设置的时间  ReadTimeout


#7.认证设置
import requests
from requests.auth import HTTPBasicAuth
r = requests.get("http://120.27.34.24:9001",auth = HTTPBasicAuth('user','123'))
# r = requests.get("http://120.27.34.24:9001",auth = {'user','123'})   #这种不需要导入HTTPBasicAuth
print(r.status_code)




