# -*- coding: utf-8 -*-
import scrapy
from img.items import *
class ImgImgSpider(scrapy.Spider):
    name = 'img_img'
    # allowed_domains = []
    # start_urls = ['https://cn.bing.com/images/async?q=%E8%8C%83%E5%86%B0%E5%86%B0&first=1&count=10&relo=4&relp=2&lostate=c&mmasync=1&dgState=c*6_y*1668s1538s1494s1697s1576s1592_i*40_w*202&IG=31DB8C32719340A1BBC6490BE601A861&SFX=2&iid=images.5747']
    start_urls = ['https://cn.bing.com/images/async?q=%E7%8C%AA&first=2&count=10&relo=100&relp=100&lostate=c&mmasync=1&dgState=c*6_y*1668s1538s1494s1697s1576s1592_i*40_w*202&IG=31DB8C32719340A1BBC6490BE601A861&SFX=2&iid=images.5747']
    def parse(self, response):
        self.parse_index = 0
        urls = response.css('ul.dgControl_list ')
        for i in urls:
            imgurls = i.css('img.mimg::attr(src)').extract()
            item = ImgItem()
            item['image_urls'] = imgurls
            yield item
        if self.parse_index <= 10:
            self.parse_index += 1
            print(self.parse_index)
            # next_page = "https://cn.bing.com/images/async?q=%E8%8C%83%E5%86%B0%E5%86%B0&first={0}&count=10&relo=4&relp=2&lostate=c&mmasync=1&dgState=c*6_y*1668s1538s1494s1697s1576s1592_i*40_w*202&IG=31DB8C32719340A1BBC6490BE601A861&SFX=2&iid=images.5747".format(parse_index)
            next_page = 'https://cn.bing.com/images/async?q=%E7%8C%AA&first={0}&count=10&relo=100&relp=100&lostate=c&mmasync=1&dgState=c*6_y*1668s1538s1494s1697s1576s1592_i*40_w*202&IG=31DB8C32719340A1BBC6490BE601A861&SFX=2&iid=images.5747'.format(self.parse_index)
            yield response.follow(next_page, self.parse)