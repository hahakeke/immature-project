# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

import pymysql


class TencentPipeline(object):
    def __init__(self):
        self.file = codecs.open('tencent.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + '\r\n'
        self.file.write(content)
        return item

    def spider_closed(self, spider):
        self.file.close()

class PymysqlPipeline(object):
    #使用pymysql插入数据库
    def __init__(self):
        self.conn = pymysql.Connect(host = "localhost",port = 3306,user = "wk",passwd = "wakewk",db = "tencent",charset = 'utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
                insert into tencent(PostName,LocationName,Responsibility,PostURL)
                values (%s,%s,%s,%s)
                """
        self.cursor.execute(insert_sql, (item["PostName"], item["LocationName"], item["Responsibility"],item['PostURL']))
        self.conn.commit()
        return item