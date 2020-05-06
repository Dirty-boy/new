# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy import signals
from scrapy.http import HtmlResponse
from .settings import IPS_URL
import os
class DjPhoneSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DjPhoneDownloaderMiddleware(object):
    def __init__(self):
        # 实例化webdriver,使用谷歌无头浏览器
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')
        self.path = './dj_phone/chromedriver.exe'

        print(os.getcwd())
        self.driver = webdriver.Chrome(executable_path=self.path, chrome_options=self.chrome_options)
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):

        self.driver.get(url=request.url)
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        return HtmlResponse(url=request.url, body=self.driver.page_source, request=request, encoding='utf-8', status=200)


    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        request.meta['proxy'] = random.choice(self.ip())
        return request

    @staticmethod
    def ip():
        ips_list = []
        ips_url = IPS_URL
        response = requests.get(ips_url).json()
        ip_data = response.get('data')
        for ip in ip_data:
            ips_list.append(f'http://{ip["IP"]}')
        return ips_list


    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
