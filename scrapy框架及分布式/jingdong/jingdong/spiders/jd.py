# -*- coding: utf-8 -*-
import json
import re

import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://book.jd.com/']

    def parse(self, response):
        pat = re.compile('navFirst:\s(.*?),\s+navTh')
        pat1 = re.compile('navThird\d+:\s(.*?)\s+navTh')
        sort_list1 =re.findall(pat,response.body.decode("unicode_escape"))
        sort_list2 = re.findall(pat1,response.body.decode("unicode_escape"))
        sort_list1 = sort_list1 + sort_list2
        sort_list = []
        for lis in sort_list1:
            if len(lis) > 0:
                print(type(lis))
                print(lis)
                sort_list =sort_list.append(lis)
        print(len(sort_list))
        # data = json.loads(sort_list)
        #         # print(data)
