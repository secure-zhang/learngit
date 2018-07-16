# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Spider,Request
from zhihuuser.items import *
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu1'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']

    start_user = 'excited-vczh'
    # 用户详情
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'locations,allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'
    # 关注列表
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    # 粉丝列表
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'

    def start_requests(self):
        # 重写父类起始函数
        # 用户的详细信息
        yield Request(self.user_url.format(user=self.start_user,include=self.user_query),callback=self.parse_user)
        # 用户的关注列表
        yield Request(self.follows_url.format(user=self.start_user,include=self.follows_query,offset=0,limit=20),callback=self.parse_follows)
        # 用户的粉丝列表
        yield Request(self.followers_url.format(user=self.start_user,include=self.followers_query,offset=0,limit=20),callback=self.parse_followers)
    def parse_user(self,response):
        # 用户详细信息
        result = json.loads(response.text) # 解码
        user_item = UserItem()
        if 'data' in result.keys():
            for field in user_item.fields:
                if field in result.keys():  # result.keys() 键
                    user_item[field] = result.get(field)
            yield user_item
        # 该用户的关注列表
        yield Request(self.follows_url.format(user=result.get('url_token'),include=self.follows_query,offset=0,limit=20),callback=self.parse_followers)
        # 该用户的粉丝列表
        yield Request(self.followers_url.format(user=result.get('url_token'),include=self.followers_query,offset=0,limit=20),callback=self.parse_user)
    def parse_follows(self,response):
        # 用户关注列表
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                # 这一页关注列表的每一个用户的信息
                url_token = result.get('url_token')
                yield Request(self.user_url.format(user=url_token,include=self.user_query),callback=self.parse_user)
        # if 'paging' in results.keys():
        #     paging = results.get('paging')
        #     is_end = paging.get('is_end')
        #     if is_end == False:
        #         # 如果不是尾页,那么就不停获取下一页关注列表
        #         next_page = paging.get('previous')
        #         yield Request(next_page,self.parse_follows)
    def parse_followers(self,response):
        # 用户粉丝列表
        results = json.loads(response.text)
        if 'data' in results.keys():
            for result in results.get('data'):
                # 这一页关注列表的每一个用户的信息
                url_token = result.get('url_token')
                yield Request(self.user_url.format(user=url_token,include=self.user_query),callback=self.parse_user)
        # if 'paging' in results.keys():
        #     paging = results.get('paging')
        #     is_end = paging.get('is_end')
        #     if is_end == False:
        #         # 如果不是尾页,那么就不停获取下一页关注列表
        #         next_page = paging.get('previous')
        #         yield Request(next_page,self.parse_follows)