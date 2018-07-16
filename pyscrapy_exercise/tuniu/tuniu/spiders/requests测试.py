# # import requests
# # url = 'http://s.tuniu.com/search_complex/whole-nj-0-%E5%8C%97%E4%BA%AC/'
# # html = requests.get(url)
# # print(html.text)
# def start_requests(self):
#     urls = 'http://s.tuniu.com/search_complex/whole-nj-0-%E5%8C%97%E4%BA%AC/'
#     yield scrapy.Request(url=urls, callback=self.parse)
#
#
# def parse(self, response):
#     html = response.css('title::text').extract()
#     print(html)