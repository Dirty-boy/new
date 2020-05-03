# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import redis

class APipeline(object):
    rds = None
    def open_spider(self,spider):
        self.rds = redis.Redis(host='127.0.0.1',port=6379,db=7)
    def process_item(self, item, spider):
        print(item)
        self.rds.lpush(item['cap'],item)
        return item
