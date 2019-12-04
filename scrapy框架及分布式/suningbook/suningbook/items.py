# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SuningbookItem(scrapy.Item):
    # define the fields for your item here like:
    m_title = scrapy.Field()
    sub_title = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    publish_date = scrapy.Field()
    url = scrapy.Field()
    price = scrapy.Field()
    # store_name = scrapy.Field()
