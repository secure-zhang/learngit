# -*- coding: utf-8 -*-
import scrapy


class BaikeSpider(scrapy.Spider):
    name = 'baike'
    allowed_domains = ['csdn.net']
    start_urls = ['https://blog.csdn.net/dqcfkyqdxym3f8rb0/article/details/80179600']

    def parse(self, response):
        print('8' * 80)
        for i in response.css('div.blog-content-box'):
            bk = i.css('h6.title-article::text').extract_first()
            yield {
                'name': bk,
            }

