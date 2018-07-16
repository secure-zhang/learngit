# -*- coding: utf-8 -*-
import scrapy
import zhaopin_demo.ip_proxy as ips
import zhaopin_demo.user_agent as user_agent
import re
from zhaopin_demo.items import *
class MyjobSpider(scrapy.Spider):
    name = 'myjob'
    allowed_domains = ['51job.com']
    start_urls = ['http://51job.com/']
    count = 0
    def start_requests(self):
        url='https://search.51job.com/list/010000,000000,0000,00,9,99,%25E5%25BC%2580%25E5%258F%2591,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
        request = scrapy.Request(url=url,callback=self.parse,meta={'proxy':ips.get_ip_proxy()})
        request.headers.setdefault('User-Agent', user_agent.get_user_agent())
        yield request
    def parse(self, response):
        hrefs = response.css('div.el>p>span>a::attr("href")').extract()
        for href in hrefs:
            request = scrapy.Request(url=href,callback=self.detail,meta={'proxy':ips.get_ip_proxy()})
            request.headers.setdefault('User-Agent', user_agent.get_user_agent())
            yield request

        #next_page = response.xpath('//dw_page//ul/li[last()]/a').css('::attr("href")').extract_first()
        next_page = response.xpath('//li[@class="bk"][last()]/a/@href').extract_first()

        if self.count < 5:
            request = scrapy.Request(url=next_page,callback=self.parse,meta={'proxy':ips.get_ip_proxy()})
            request.headers.setdefault('User-Agent', user_agent.get_user_agent())
            yield request
            self.count+=1
    def detail(self,response):
        zwmc = response.css('div.cn>h1::text').extract_first()
        gsmc = response.css('div.cn>p.cname>a::text').extract_first()
        # basic = response.css('div.t1')
        # zwyx=basic.xpath('./li[1]/strong/text()').extract_first()
        zwyx= response.css('div.cn>strong::text').extract_first()
        # gzdd = basic.xpath('./li[2]/strong/a/text()').extract_first()
        gzdd = response.css('div.cn>h1>span::text').extract_first()
        # gwxq = response.css('div.tab-inner-cont').extract_first()
        gwxq = response.css('div.bmsg.job_msg.inbox').extract_first()

        p='<[a-z][^/]*>|</[a-z\s\d]*>|\\n+'
        gwxq=re.subn(p,"",gwxq)
        item = ZhaopinDemoItem()
        item['zwmc']=zwmc
        item['gsmc']=gsmc
        item['zwyx']=zwyx
        item['gzdd']=gzdd
        item['gwxq']=gwxq
        yield item


