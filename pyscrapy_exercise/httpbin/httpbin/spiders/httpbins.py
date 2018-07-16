# -*- coding: utf-8 -*-
import scrapy


class HttpbinsSpider(scrapy.Spider):
    name = 'httpbins'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/']

    def parse(self, response):
        print(response.text)
