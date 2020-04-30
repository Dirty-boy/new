# -*- coding: utf-8 -*-
import scrapy
from bian.items import BianItem

class BianImgSpider(scrapy.Spider):
    name = 'bian_img'
    # allowed_domains = ['http://pic.netbian.com/']
    start_urls = ['http://pic.netbian.com/']
    my_page  = 1
    max_page = 1196
    change_page_url = 'http://pic.netbian.com/index_%s.html'
    def parse(self, response):
        ul = response.xpath('/html/body/div[2]/div[1]/div[3]/ul')
        img_url = ul.xpath('./li/a/@href').extract()

        for  i in range(len(img_url)):
            this_url = self.start_urls[0] + img_url[i]
            yield scrapy.Request(url=this_url,callback=self.parse_second)
        if self.my_page <= self.max_page:
            self.my_page += 1
            if self.my_page%100 == 0:
                import time
                time.sleep(30)
            new_url = self.change_page_url%self.my_page
            yield scrapy.Request(url=new_url,callback=self.parse)

    def parse_second(self,response):
        name = response.xpath('//div[@class="photo-hd"]/h1//text()').extract_first()
        img_url = response.xpath('//div[@class="photo-pic"]/a/img/@src').extract_first()
        img_url = 'http://pic.netbian.com' + img_url
        print(img_url)
        item = BianItem()
        item['name'] = name +img_url[-4:]
        item['url'] = img_url
        yield item

