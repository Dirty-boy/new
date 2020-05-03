# -*- coding: utf-8 -*-
import scrapy

from A.items import AItem
class KjSpider(scrapy.Spider):
    name = 'kj'
    # allowed_domains = ['http://www.stdaily.com/qykj/qianyan/jryw.shtml']
    start_urls = ['http://www.stdaily.com/qykj/qianyan/jryw.shtml']
    main_url = 'http://www.stdaily.com/'
    def parse(self, response):
        li_url = response.xpath('//div[@class="xwlist"]//li/a//@href').extract()
        li_title = response.xpath('//div[@class="xwlist"]//li/a//text()').extract()
        li_time = response.xpath('//div[@class="xwlist"]//li/span//text()').extract()
        # print(li_url,li_title,li_time)
        print(len(li_url),len(li_title),len(li_time))

        for i in range(len(li_url)):
            item = AItem()
            item['url'] = self.main_url + li_url[i]
            item['title'] = li_title[i]
            item['time'] = li_time[i]
            yield item