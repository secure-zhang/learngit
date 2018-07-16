# -*- coding: utf-8 -*-
import scrapy
from kgc_demo.items import *

class KekeSpider(scrapy.Spider):
    name = 'keke'
    allowed_domains = ['kgc.cn']
    start_urls = ['http://www.kgc.cn/list/230-1-6-9-9-0.shtml']

    def parse(self, response):
        ke = response.css('div.course_info')
        for i in ke:
            name = i.css('div.f16 a::text').extract_first()
            peoples = i.css('span.course-pepo::text').extract_first()
            prices = i.css('div.right span::text').extract_first()
            firstmysql = FirstMysql()
            firstmysql['name'] = name
            firstmysql['peoples'] = peoples
            firstmysql['prices'] = prices
            yield firstmysql
        next_page = response.css('div.pager li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page,self.parse)

