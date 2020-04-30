# -*- coding: utf-8 -*-
import scrapy
from bz.items import TestStItem
from datetime import datetime
import time
"""
http://img.netbian.com/file/2020/0315/5967a95623959395d7e0cda38498bcd9.jpg

http://img.netbian.com/file/2020/0315/5967a95623959395d7e0cda38498bcd9.jpg
"""

class TestOneSpider(scrapy.Spider):
    name = 'bizhi'
    # allowed_domains = ['http://www.netbian.com/1920x1080/']
    start_urls = ['http://bizhi.bcoderss.com/']  # 全站
    # start_urls = ['http://bizhi.bcoderss.com/tag/动漫/']
    # all_list = []
    other_url = 'http://bizhi.bcoderss.com/page/%s/'  # 全站
    # other_url = 'http://bizhi.bcoderss.com/tag/动漫/page/%s/'
    get_page = 10   # 爬取多少页  #  最大页数 510+ # 5页相当于更新
    n = 1 # 当前页面
    def parse(self, response):
        print(f'第{self.n}页开始:')
        print(f'开始时间:{datetime.now()}')
        start = time.time()
        img = response.xpath('//ul[@id="main"]/li/a/img/@src').extract()
        for i in img:
            d= i.split('-260x534')
            img_url = ''.join(d)
            item = TestStItem()
            tt = img_url.split('/')[-1]
            item['title'] = tt
            item['url'] = img_url
            yield item
        print('爬取结束,总耗时:',time.time()-start)
        if self.n <= self.get_page-1:
            self.n += 1
            new_url = self.other_url % self.n
            yield scrapy.Request(url=new_url, callback=self.parse)



