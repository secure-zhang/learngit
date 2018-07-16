# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhaopinDemoItem(scrapy.Item):
    '''职位名称 公司名称 职位月薪  工作地点 岗位需求'''
    job_title = scrapy.Field()
    Company= scrapy.Field()
    price = scrapy.Field()
    # address = scrapy.Field()
    info = scrapy.Field()