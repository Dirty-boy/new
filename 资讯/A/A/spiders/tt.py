# -*- coding: utf-8 -*-
import scrapy
from A.items import AItem

class TtSpider(scrapy.Spider):
    name = 'tt'
    # allowed_domains = [']
    start_urls = ['http://www.stdaily.com/qykj/index.shtml']
    second_url = []
    main_url = 'http://www.stdaily.com/'

    def parse(self, response):
        once_url = response.xpath('//div[@class="navfl"]/ul/li/a//@href').extract()
        once_cap = response.xpath('//div[@class="navfl"]/ul/li/a//text()').extract()
        for  i in range(len(once_url)):
            item = AItem()
            item['cap'] = once_cap[i]
            once_get_url = self.main_url + once_url[i]
            yield scrapy.Request(url=once_get_url,callback=self.parse_second,meta={'item':item})

    def parse_second(self,response):
        # print(response)
        item = response.meta['item']
        title_url = response.xpath('//div[@class="main"]//h3/a//@href').extract()
        title = response.xpath('//div[@class="main"]//h3/a//text()').extract()
        title_time = response.xpath('//div[@class="main"]//span//text()').extract()

        for i in range(len(title_url)):
            item['url'] = self.main_url + title_url[i]
            item['title'] = title[i]
            item['time'] = ' '.join(title_time[i].split()[0:])
            yield item
