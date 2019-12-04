# -*- coding: utf-8 -*-
import scrapy


class GitSpider(scrapy.Spider):
    name = 'git'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):

        pass
