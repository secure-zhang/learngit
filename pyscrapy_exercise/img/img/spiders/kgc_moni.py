import scrapy

class LoginSpider(scrapy.Spider):
    name = 'logintest'
    start_urls = ['http://www.kgc.cn/member/login?redirect_url=http%3A%2F%2Fwww.kgc.cn%2Fmy%2FjobOE.shtml']
    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            # 需要找到用户名和密码框的标签
            formdata={'KgcForm_models_LoginForm[identity]': '951428148@qq.com', 'KgcForm_models_LoginForm[password]': '123456'},
            callback=self.after_login
        )

    def after_login(self, response):
        # check login succeed before going on
        error = response.css('div#KgcForm_models_LoginForm_password_em_::text').extract_first()
        if error is None:
            next_page = response.css('div.courseInfo a::attr(href)').extract_first()
            if next_page is not None:
                yield response.follow(next_page, self.parse2)
        else:
            print('12312')
    def parse2(self,response):
        ul = response.css('ul.common-learn-line').xpath('li')
        for i in ul:
            name = i.css('strong::text').extract_first()
            cont = i.css('div.zj-tip::text').extract_first()
            pylist = i.css('dl dt a.course-name::text').extract()
        yield response.follow('http://www.kgc.cn/jobs/course?id=5973&product_id=24768',self.parse3)
    def parse3(self,response):

        # continue scraping with authenticated session...
