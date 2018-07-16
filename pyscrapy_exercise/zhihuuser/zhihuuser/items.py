# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuuserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class UserItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    url_token = scrapy.Field()
    name = scrapy.Field()
    avatar_url = scrapy.Field() # 图片连接
    headline = scrapy.Field()   # 签名
    # locations = scrapy.Field()  # 地址
class FollowsItem(scrapy.Item):
    pass
    # is_followed = scrapy.Field()
    # avatar_url_template = scrapy.Field()
    # answer_count = scrapy.Field()
    # is_following = scrapy.Field()
    # url = scrapy.Field()
    # url_token = scrapy.Field()
    # id = scrapy.Field()
    # articles_count = scrapy.Field()
    # name = scrapy.Field()
    # headline = scrapy.Field()

