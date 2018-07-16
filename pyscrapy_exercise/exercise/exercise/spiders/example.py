# -*- coding: utf-8 -*-
import scrapy

from exercise import items

class ExampleSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        print('-' * 80)
        for i in response.css('.quote'):
            item = items.ExerciseItem()
            text = i.css('span.text::text').extract_first()
            author = i.css('.author::text').extract_first()
            tags = i.css('a.tag::text').extract()
            if text is None:
                text = ' '
            if author is None:
                author = ' '
            if tags is None:
                tags = ' '
            item['text'] = text
            item['author'] = author
            item['tags'] = str(tags)
            yield item
        next_page = response.css('.next > a:nth-child(1)::attr(href)').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            # 俩种回调方式
            yield response.follow(url,self.parse)
            yield scrapy.Request(url=url,callback=self.parse)
