# -*- coding: utf-8 -*-
import scrapy,time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

class AmaSpider(RedisCrawlSpider):
    name = 'ama'
    # allowed_domains = ['amason.cn']
    # start_urls = ['http://amason.cn/']
    redis_key = 'amasonbook'

    rules = (
        #获取大标签url和中标签url地址
        Rule(LinkExtractor(restrict_xpaths=("//*[@id='leftNav']/ul[4]/ul/div/li/span/a",)), follow=True),
        #获取图书列表页图书的url
        Rule(LinkExtractor(restrict_xpaths=("//div[@class='a-row a-spacing-small']/div/a",)),callback='parse_item'),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']",)), follow=True),
            )

    def parse_item(self, response):
        item = {}
        item["book_url"] = response.url
        item["book_cate"] = response.xpath("//*[@id='wayfinding-breadcrumbs_feature_div']/ul/li[5]/span/a/text()").extract_first()
        item["book_title"] = response.xpath("//div[@id='booksTitle']/div/h1/span/text()").extract_first().strip()
        item["book_price"] = response.xpath("//tr[@class='kindle-price']/td[2]/span/text()").extract_first().strip()
        item["book_author"] = response.xpath("//div[@id='bylineInfo']/span[1]/a/text()").extract_first().strip()
        item["book_publish_date"] = response.xpath("//div[@class='buying']/span[2]/text()").extract_first().strip()
        item["book_desc"] = response.xpath("//noscript/div/text()").extract()
        item["book_desc"] = [i.strip() for i in item["book_desc"] if len(i.strip())>0 and i !='海报']
        print(item)
        # return item
