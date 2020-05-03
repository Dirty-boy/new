# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GwSpider(CrawlSpider):
    name = 'gw'
    start_urls = ['http://www.stdaily.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*.shtml'), callback='parse_item', follow=True),

    )
    n = 0
    def parse_item(self, response):
        down = response.request.url.split('/')[3:]
        if len(down) <= 4:
            pass

        else:
            self.n += 1
            print(response)

        print(self.n)

