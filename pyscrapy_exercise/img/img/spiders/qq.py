# -*- coding: utf-8 -*-
import scrapy
class ImgImgSpider(scrapy.Spider):
    name = 'qq'
    # allowed_domains = []
    start_urls = ['https://i.qq.com/']
    def parse(self, response):
        kj = response.css('div.fn-feed-container').xpath('li')
        for i in kj:
            a = i.css('div.user-pto a::attr(href)').extract()
            for q in a:
                print(q)
            yield {
                'a': a
            }