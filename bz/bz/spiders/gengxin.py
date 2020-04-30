# -*- coding: utf-8 -*-
import scrapy
from bz.items import TestStItem


class GengxinSpider(scrapy.Spider):
    name = 'gengxin'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://bizhi.bcoderss.com/']

    def parse(self, response):
        img = response.xpath('//ul[@id="main"]/li/a/img/@src').extract()
        for i in img:
            d = i.split('-260x534')
            img_url = ''.join(d)
            item = TestStItem()
            tt = img_url.split('/')[-1]
            item['title'] = tt
            item['url'] = img_url
            yield item
