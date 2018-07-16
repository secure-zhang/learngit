# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import pymysql
import scrapy


class KgcDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class FirstMysql(scrapy.Item):
    name = scrapy.Field()
    peoples = scrapy.Field()
    prices = scrapy.Field()
# class KeItem(scrapy.Item):
#     name = scrapy.Field()
#     price = scrapy.Field()
#     counts = scrapy.Field()
