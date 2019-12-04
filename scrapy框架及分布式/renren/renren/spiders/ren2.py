# -*- coding: utf-8 -*-
import re

import scrapy


class Ren2Spider(scrapy.Spider):
    name = 'ren2'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/972832035']

    def start_requests(self):
        cookies = "anonymid=k2szvd293mq66o; depovince=GW; _r01_=1; JSESSIONID=abc1-Jq8ClXuccEugxv5w; ick_login=380e2a16-b2bd-4c94-a11f-61dda2362e68; ick=f8cc19f6-9251-4381-904e-0237b32871ef; XNESSESSIONID=b7b7efd920ae; jebe_key=e0a90f96-5f5f-48e7-a7f6-80f41efca67d%7C4a0e98b7fb70f033736e269c20982018%7C1573390457177%7C1%7C1573390460978; jebe_key=e0a90f96-5f5f-48e7-a7f6-80f41efca67d%7C4a0e98b7fb70f033736e269c20982018%7C1573390457177%7C1%7C1573390460981; wp_fold=0; wp=0; first_login_flag=1; ln_uact=15068781790; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=a82f5fa4-22eb-4f3b-8a3f-ea959a783159|||||; _de=EA673758EDEAAC07AA0E26444A0432B6; p=c104e480936c6ac403be59105a46f2f35; t=2043301322302456166253ea8084dc0c5; societyguester=2043301322302456166253ea8084dc0c5; id=972832035; xnsid=aa8ea5ba; ver=7.0; loginfrom=null"
        cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies=cookies
                             )

    def parse(self, response):
        # with open("dd.html",'w',encoding='utf-8') as f:
        #     f.write(response.body.decode())
        #     f.close()
        print(re.findall("柯达",response.body.decode()))


