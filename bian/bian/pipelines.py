# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
class ImgsPipiLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        print(f'正在请求: {item["url"]}')
        yield scrapy.Request(url=item['url'],meta={'item':item})
    def file_path(self, request, response=None, info=None):
        filePath = request.meta['item']['name']
        print(f'已获取图片名称:{filePath}')
        return filePath

    def item_completed(self, results, item, info):
        return item