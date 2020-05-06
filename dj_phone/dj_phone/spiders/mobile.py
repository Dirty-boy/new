# -*- coding: utf-8 -*-
import scrapy

from .. import settings
from ..items import DjPhoneItem

class MobileSpider(scrapy.Spider):
    name = 'mobile'
    # allowed_domains = ['www.jd.com']
    base_url = r'https://search.jd.com/Search?keyword=%s&wq=%s&page=%d&s=%d&click=0'
    page = 1
    data = 30

    def start_requests(self):
        for i in range(1, settings.MAX_PAGE):
            url = self.base_url % (settings.KEYWARDS, settings.KEYWARDS, self.page, self.data)
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
            self.page += 2
            self.data += 30

    def parse(self, response):
        li_list = response.xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div[2]/ul/li')
        for li in li_list:
            items = DjPhoneItem()
            title = li.xpath('./div/div[4]/a/em/text()').extract_first()
            price = li.xpath('./div/div[3]/strong/i/text()').extract_first()
            info = li.xpath('./div/div[4]/a/@title').extract_first()
            comment = li.xpath('./div/div[5]/strong/a/text()').extract_first()
            shop = li.xpath('./div/div[7]/span/a/text()').extract_first()
            items['title'] = title
            items['price'] = price
            items['info'] = info
            items['comment'] = comment
            items['shop'] = shop
            yield items
