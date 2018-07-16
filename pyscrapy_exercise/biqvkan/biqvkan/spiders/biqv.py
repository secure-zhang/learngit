# -*- coding: utf-8 -*-
import scrapy


class BiqvSpider(scrapy.Spider):
    name = 'biqv'
    allowed_domains = ['www.biqukan.com']
    start_urls = ['http://www.biqukan.com/']

    def parse(self, response):
        pass
