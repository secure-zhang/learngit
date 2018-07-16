# -*- coding: utf-8 -*-
import scrapy
import re
from zhaopin_demo.items import *
class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    a = 0
    start_urls = ['https://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88&p=1&isadv=0']
    def parse(self, response):
        zwlist = response.css('div#newlist_list_content_table td.zwmc')
        for i in zwlist:
            '''获取a标签➕b标签的名字'''
            # text = i.extract()
            # text = re.findall('<a .* target="_blank">(.+)</a>',text)
            # if len(text) == 1:
            #     text = re.sub('</?b>','',text[0])
            # print(text)
            next_page = i.css(' a::attr(href)').extract_first()
            yield response.follow(next_page,self.parse2)
        next_page2 = response.css('a.next-page::attr(href)').extract_first()
        if self.a <= 3:
            self.a += 1
            print('*'*200)
            yield response.follow(next_page2, self.parse)

    def parse2(self,response):
        job_title = response.css('div.fl h1::text').extract_first()
        Company = response.css('div.fl h2 a::text').extract_first()
        price = response.css('ul.terminal-ul.clearfix li strong::text').extract_first()
        # address = response.css('ul.terminal-ul.clearfix').xpath('./li[2]/strong/text()').extract()
        # info = response.css('div.tab-inner-cont').extract_first()
        info = response.css('div.terminalpage-main>div.tab-cont-box').xpath('div[1]/p/text()').extract()
        info = ' '.join(info)
        p = '<[a-z][^/]*>|</[a-z\s\d]*>'
        info = re.sub('\n','',info)
        info = re.sub(p,'',info)
        item = ZhaopinDemoItem()
        item['job_title'] = job_title
        item['Company'] = Company
        item['price'] = price
        item['info'] = info
        yield item

