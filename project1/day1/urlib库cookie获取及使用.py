#获取cookie
# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# print(response.status)
# for item in cookie:
#     print(item.name+"="+item.value)


#当cookie保存为本地文件(火狐浏览器1)
# import http.cookiejar,urllib.request
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# # cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# print(response.status)
# cookie.save(ignore_discard=True,ignore_expires=True)

#当cookie保存为本地文件(2)
# import http.cookiejar,urllib.request
# filename = "cookie1.txt"
# cookie = http.cookiejar.LWPCookieJar(filename)
# # cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open("http://www.baidu.com")
# print(response.status)
# cookie.save(ignore_discard=True,ignore_expires=True)

#本地cookie文件的加载
import http.cookiejar,urllib.request
filename = "cookie1.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
cookie.load('cookie1.txt',ignore_discard=True,ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode('utf-8'))
