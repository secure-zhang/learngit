# -*- coding: utf-8 -*-
import scrapy
# from kgc_two.items import *
class KgcexerSpider(scrapy.Spider):
    name = 'kgcExer'    # 蜘蛛的名字
    allowed_domains = ['kgc.cn']        # 域名
    start_urls = ['http://kgc.cn/']     # 网址链接

    def parse(self, response):
        '''解析数据'''
        obj = response.css('ul.job-list li')    # 获取爬取数据所在的html
        for o in obj:
            name = o.css('p a::text').extract_first()   # 此时获取名字
            job = o.xpath('p/text()').extract_first()
            # name = o.css('p a::text').extract_first()
            # job = o.css('p.font12::text').extract_first()
             # 将爬去下的内容存储到item
            # item = FirstDemoItem()
            # item['name'] = name
            # item['job'] = job
            # yield item
            yield {
                'name':name
            }
            print(name)