#pyquery使用

html ="""<html lang="zh-CN" class="ua-windows ua-ff69 book-new-nav">
  <head>
    <p>
        <meta charset="utf-8">
        <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    </p>
    <div1>
    <div id="container">
        <div class="list">
        <li class="kkd chv" href="wwww.baidu.com"><a>meta http-equiv="Pragma" content="no-cache"</a>1nishishenmerena </li>
        <li class="www"><meta http-equiv="Pragma" content="no-cache">2mahsnemedongmeia</li>
        <li class="ghl"><meta http-equiv="Pragma" content="no-cache">3madongshenme</li>
        <li class-"jjs"><meta http-equiv="Pragma" content="no-cache">4domhgdomhdmei</li>
        </div>
        <div class="list"><a class="tt">meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"</a></div>
    </div></div1>
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    </head>"""
#字符串初始化
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('p'))

#url初始化
# from pyquery import PyQuery as pq
# doc = pq(url="http://www.baidu.com")
# print(doc('head'))

#文件初始化
# from pyquery import PyQuery as pq
# doc = pq(filename='demo.html')
# print(doc('p'))

#基本CSS选择器
# from pyquery import PyQuery as pq
# doc = pq(html)
# print(doc('#container .list li'))   ##container根据ID查找，class属性li标签

# from pyquery import PyQuery as pq
# doc = pq(html)
# items = doc('.list')
# print(type(items))
# print(items)
# lis = items.find('li')
# print(type(lis))
# print(lis)

#获取子节点，父节点，祖先节点，兄弟节点
# from pyquery import PyQuery as pq
# doc = pq(html)
# li = doc(".kkd")
# print(li)
# print(type(li))
# print(li.items())
# print(li.parent())

# print(li.parents("#container"))
# print(li.siblings(".ghl"))
# print(li.attr('href'))    #获取属性
# print(li.attr.href)
# print(li.text())
# print(li.html())




#DOM操作-----------------------------------------------------
#addClass,removeClass添加，删除class操作
from pyquery import PyQuery as pq
doc = pq(html)
li = doc(".chv")
print(li.text())
# li.remove_class('chv')    #删除class中的chv
# print(li)
# li.add_class('chv')
# print(li)
#atte,css添加属性和添加style属性
# li.attr('name','dada')
# print(li)
# li.css('front-size','14px')
# print(li)
#remove操作与find（）结合删除某个标签
li.find('a').remove()
print(li.text())





