# -*- coding: utf-8 -*-
import json

import scrapy
import re
from tencent.items import TencentItem
from scrapy import Request


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['careers.tencent.com']
    page = 1
    url = 'http://careers.tencent.com/tencentcareer/api/post/Query?pageIndex='+str(page)+'&pageSize=10'
    start_urls = [url]

    def parse(self, response):
        print('正在获取第%d页的数据：'%self.page,response.url)
        data = response.body.decode()
        pat1 = '"RecruitPostName":"(.*?)","CountryName"'
        pat2 = '"LocationName":"(.*?)","BGName"'
        pat3 = '"Responsibility":"(.*?)"'
        pat4 = '"PostURL":"(.*?)"'
        PostName = re.findall(pat1,data)
        LocationName = re.findall(pat2,data)
        Responsibility = re.findall(pat3,data)
        PostURL = re.findall(pat4,data)
        for i in range(len(PostName)):
            item = TencentItem()
            item["PostName"] = PostName[i]
            item["LocationName"] = LocationName[i]
            item["Responsibility"] = Responsibility[i]
            item["PostURL"] = PostURL[i]
            yield item
        self.page += 1
        next_url = 'http://careers.tencent.com/tencentcareer/api/post/Query?pageIndex='+str(self.page)+'&pageSize=10'
        yield Request(next_url,dont_filter=True,callback=self.parse)

