import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                    # 因为前面的还是一个对象所以需要extract_first 提取,抽取数据中的第一个
                'author': quote.xpath('span/small/text()').extract_first(),
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        print(next_page)
        if next_page is not None:
            yield response.follow(next_page, self.parse)
# a = '20150616'
# b = a[0:4]+'-'+a[4:6]+'-'+a[6::]
# print(type(b))