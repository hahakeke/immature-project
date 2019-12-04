#Beautifulsoup补充

from bs4 import BeautifulSoup
html ="""<html lang="zh-CN" class="ua-windows ua-ff69 book-new-nav">
  <head>
    <p>
        <meta charset="utf-8">
        <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    </p>
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    </head>"""
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# print(list(enumerate(soup.head.descendants)))    #获取子孙节点
# print(soup.p.parent)     #获取父节点
# print(soup.p.parents)   #获取父祖节点
print(list(enumerate(soup.p.next_sibling)))  #获取下一个兄弟节点（上一个用previous_sibling）



#find_all的使用
# find_all(name,attar,recursive,text,**kwargs) 返回所有元素
print(soup.find_all(attrs={'id':'list-1'}))   #案例 id,class属性可直接查找，去掉attars =
print(soup.find_all(text='dalong'))  #案例


#find的使用
#find(name,attar,recursive,text,**kwargs)  返回单个元素


