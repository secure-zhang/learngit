# -*- coding: utf-8 -*-
import scrapy


class ZhizhuSpider(scrapy.Spider):
    name = 'zhizhu'
    allowed_domains = ['zhizhu.com']
    start_urls = ['http://zhizhu.com/']

    def parse(self, response):
        pass
