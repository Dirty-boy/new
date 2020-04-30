# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from redis import Redis
# class TestStPipeline(object):
#     #redis 操作
#     rds = None
#     def open_spider(self, spider):
#         # 开始
#         self.rds = Redis(host='127.0.0.1',port=6379,db=2)
#         print(self.rds)
#     # def close_spider(self, spider):
#     def process_item(self,item,spider):
#         # self.rds.lpush('img',f"{item['title'][0]}:{item['true_url'][0]}")
#         self.rds.sadd('壁纸',{'title':item['title'],'url':item['url']})

class ImgsPipiLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        # print(item)
        yield scrapy.Request(url=item['url'],meta={'item':item})
    #返回图片名称即可
    def file_path(self, request, response=None, info=None):
        #通过request获取meta
        item = request.meta['item']
        filePath = item['title']
        print(filePath)
        return filePath #只需要返回图片名称
    #将item传递给下一个即将被执行的管道类
    def item_completed(self, results, item, info):
        return item