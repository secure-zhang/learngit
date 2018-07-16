# -*- coding: utf-8 -*-
import scrapy


class TuSpider(scrapy.Spider):
    name = 'tu'
    # allowed_domains = ['tuniu.com']
    start_urls = ['http://s.tuniu.com/search_complex/whole-nj-0-%E5%8C%97%E4%BA%AC/']

    def parse(self, response):
        html = response.css('ul.thebox li')
        print('------------')
        for i in html:
            url = i.response.css('a')
            print(url)
            # print('------------')
