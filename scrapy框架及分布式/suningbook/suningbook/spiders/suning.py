# -*- coding: utf-8 -*-
import re
from copy import deepcopy

import scrapy
from scrapy import Request

from suningbook.items import SuningbookItem

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://book.suning.com/?safp=d488778a.homepage1.99345513004.61']

    def parse(self, response):
        m_titlelist = response.xpath('//div[@class="menu-list"]/div[@class="menu-item"]//h3/a/text()').extract()
        sub_menu = response.xpath('//div[@class="menu-list"]/div[@class="menu-sub"]')
        for i in range(len(m_titlelist)):
            item = SuningbookItem()
            item['m_title'] = m_titlelist[i]
            sub_namelist = sub_menu[i].xpath('./div[@class="submenu-left"]/p[@class="submenu-item"]/a/text()').extract()
            sub_menu_url = sub_menu[i].xpath('./div[@class="submenu-left"]/p[@class="submenu-item"]/a/@href').extract()
            if len(sub_namelist) != 0:
                for x in range(len(sub_menu_url)):
                    item['sub_title'] = sub_namelist[x]
                    url = sub_menu_url[x]
                    yield Request(url,callback=self.parse_book_list,meta={'item':deepcopy(item)})
            else:
                sub_namelist = sub_menu[i].xpath('./div[@class="submenu-left"]/ul/li/a/text()').extract()
                sub_menu_url = sub_menu[i].xpath('./div[@class="submenu-left"]/ul/li/a/@href').extract()
                for y in range(len(sub_namelist)):
                    item['sub_title'] = sub_namelist[y]
                    url = sub_menu_url[y]
                    yield Request(url,callback=self.parse_book_list,meta={"item":deepcopy(item)})

    def parse_book_list(self,response):    #加载商品列表页,因为页面动态加载分上下半页，直接获取的为上半页
        item = response.meta['item']
        #获取当前的页面码，并构造下半页地址
        #获取总共页码
        count_page = re.findall('共(.*?)页，到第',response.body.decode())
        ci = re.findall('categoryId": "(.*?)",',response.body.decode())[0]
        if len(count_page)>0 :
            for cp in range(int(count_page[0])):
                up_half_page_url = "https://list.suning.com/emall/showProductList.do?ci=" + str(ci) + "&cp=" + str(cp) + "&pg=03&cc=571"
                down_half_page_url = "https://list.suning.com/emall/showProductList.do?ci="+str(ci)+"&cp="+str(cp)+"&pg=03&cc=571&paging=1&sub=0"
                yield Request(up_half_page_url,callback=self.parse_half_page,meta={"item":deepcopy(item)},dont_filter=True)
                yield Request(down_half_page_url, callback=self.parse_half_page,meta={"item": deepcopy(item)},dont_filter=True)
        else:
            cp = 0
            up_half_page_url = "https://list.suning.com/emall/showProductList.do?ci=" + str(ci) + "&cp=" + str(
                cp) + "&pg=03&cc=571"
            down_half_page_url = "https://list.suning.com/emall/showProductList.do?ci=" + str(ci) + "&cp=" + str(
                cp) + "&pg=03&cc=571&paging=1&sub=0"
            yield Request(up_half_page_url, callback=self.parse_half_page, meta={"item": deepcopy(item)},
                          dont_filter=True)
            yield Request(down_half_page_url, callback=self.parse_half_page, meta={"item": deepcopy(item)},
                          dont_filter=True)

     #获取半页商品详细地址
    def parse_half_page(self,response):
        item = response.meta["item"]
        print(item)
        half_booklist = re.findall('title=.*\s+href="(.*?)"\s+name=',response.body.decode())
        for link in half_booklist:
            link = 'http:' + link
            yield Request(link,callback=self.parse_goods_detail,meta={"item":deepcopy(item)})

    #定义爬取商品详情页
    def parse_goods_detail(self,response):
        item = response.meta["item"]
        item["url"] = response.url
        try:
            item["title"] = response.css('#itemDisplayName::text').extract()[1].strip()
        except Exception as e:
            print(e)
            item["title"] = None
        item["publish_date"] = response.xpath('//ul[@class="bk-publish clearfix"]/li[3]/span[2]/text()').extract_first()
        auth_list = response.xpath('//ul[@class="bk-publish clearfix"]/li[1]/text()').extract()
        if len(auth_list)>0:
            item["author"] = re.sub('\\r|\\n|\\t','',auth_list[0].strip())
            press_list = response.xpath('//ul[@class="bk-publish clearfix"]/li[2]/text()').extract()
            if len(press_list)>0:
                item["press"] = press_list[0].strip()
            else:
                item["press"] = None
        else:
            item["author"] = None
            press_list = response.xpath('//ul[@class="bk-publish clearfix"]/li[1]/text()').extract()
            if len(press_list)>0:
                item["press"] = press_list[0].strip()
            else:
                item["press"] = None
        #构造详情页面
        partNumber = re.findall('"partNumber":"(.*?)","context"',response.body.decode())[0]
        vendorCode = re.findall('"vendorCode":"(.*?)",',response.body.decode())[0]
        catenIds = re.findall('"catenIds":"(.*?)","catalogId"',response.body.decode())[0]
        weight = re.findall('weight":"(.*?)",',response.body.decode())[0]
        price_url = 'http://pas.suning.com/nspcsale_0_'+partNumber+'_'+partNumber+'_'+vendorCode+'_130_571_5710101_502282_1000323_9315_12499_Z001___'+catenIds+'_'+weight+'___.html'
        yield Request(price_url,callback=self.parse_price,meta={'item':deepcopy(item)})

    #定义获取价格的函数
    def parse_price(self,response):
        item = response.meta["item"]
        item["price"] = re.findall('"promotionPrice":"(.*?)","bookPrice"',response.body.decode())[0]
        print(item)






