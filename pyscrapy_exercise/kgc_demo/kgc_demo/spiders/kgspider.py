# -*- coding: utf-8 -*-
import scrapy
from kgc_demo.items import *

class KgspiderSpider(scrapy.Spider):
    name = 'kgspider'
    allowed_domains = ['kgc.cn']
    start_urls = ['http://kgc.cn/']

    def parse(self, response):
        for o in response.css('ul.job-list').xpath('./li'):
                img = o.css('p/a::people-img')
                name = o.xpath('p/a/text()').extract(),
                job = o.css('p.font12::text').extract(),
                yield {
                    'name': name,
                    'job': job,
                    # item['name']
            }
class kgcke(scrapy.Spider):
    name = 'ke'
    allowed_domains = ['kgc.cn']
    start_urls = ['http://www.kgc.cn/list/230-1-6-9-9-0.shtml/']

    def parse(self, response):
        for o in response.css('ul.job-list').xpath('./li'):
                img = o.css('p/a::people-img')
                name = o.xpath('p/a/text()').extract(),
                job = o.css('p.font12::text').extract(),
        # 导入item item = KeItem()
                yield {
                    'name': name,
                    'job': job,
                    # item['name']
            }