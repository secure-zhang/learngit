# -*- coding: utf-8 -*-
import scrapy


class KgcexerSpider(scrapy.Spider):
    name = 'kgcExer'
    allowed_domains = ['kgc.cn']
    start_urls = ['http://kgc.cn/']

    def parse(self, response):
        for o in response.css('ul.view-sec3 li div.view-tip'):
            name = o.css('p::text').extract_first()
            print(name)
            yield {
                'name': name,
            }
