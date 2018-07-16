# 使用requests + selenium + phantomjs 抓取微信公众号文章
# 抓取指定系列公众号
import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
class Downloader:
    def __init__(self):
        self.url = 'https://mp.weixin.qq.com'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
        self.index_url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%97%85%E6%B8%B8&ie=utf8&_sug_=n&_sug_type_='
        self.blank_url = 'https://mp.weixin.qq.com/profile?src=3&timestamp=1530005869&ver=1&signature=q5TnqplxAJO6Afw3pQEHFy5DttEoLazjeQe8HBJMoM2guRedrjjfR*zHjDrQ8BU9FFR*WMCAYc452yuMc*MIDw=='
        self.blank_urls = []
        self.tit_urls = []
        self.titles = None
        self.content = []
        self.blank_name = None
        self.wx_name = None
    def get_blank_url(self):
        '''获取公众号地址'''
        html = requests.get(self.index_url,self.headers).text
        soup = BeautifulSoup(html,'lxml')
        soup = soup.select('.news-list2 li a')
        for i in soup:
            blank_url = i.attrs['href']
            if len(blank_url) > 20: # 因为有一部分为js代码 所以筛选
                self.blank_urls.append(blank_url)
    def get_title_url(self):
        '''获取文章url,因为是js加载的所以使用selenium'''
        time.sleep(10)
        browser = webdriver.PhantomJS()
        browser.get(self.blank_url)
        # 执行js得到整个页面内容
        html = browser.execute_script("return document.documentElement.outerHTML")
        soup = BeautifulSoup(html,'lxml')
        try:
            self.blank_name = soup.select('.profile_nickname')[0].string
            self.wx_name = soup.select(('.profile_account'))[0].string
            media = soup.find_all(class_='weui_media_bd')
            for i in media:
                tit_url = self.url+i.h4.attrs['hrefs'].strip()
                self.tit_urls.append(tit_url)
        except:
            print('需要输入验证码')
    def get_content(self,tit_url):
        '''获取内容'''
        html = requests.get(tit_url,self.headers).text
        soup = BeautifulSoup(html,'lxml')
        self.titles = soup.find(id='activity-name').string.strip()

        span_list = soup.select('#js_content p span')
        for i in span_list:
            span = i.string
            if span:
                self.content.append(span+'\n')
        self.myfile()
    def myfile(self):
        with open('file.txt','a',encoding='utf-8') as f:
                f.write(self.blank_name) # 公众号
                f.write('\n')
                f.write(self.wx_name)  # 微信号
                f.write('\n')
                f.write(self.titles)   # 标题
                f.write('\n')
                f.write(str(self.content))  # 内容
                f.write('\n')
                f.write(self.tit_urls[0]) # 链接
                f.write('\n')

import pymysql
class My_sql:
    def __init__(self,blank_name,wx_name,title,content,tit_urls):
        self.tit_urls = tit_urls
        self.blank_name = blank_name
        self.wx_name = wx_name
        self.title = title
        self.connect = content
        # 连接数据库
        print('连接数据库')
        self.connect = pymysql.connect(
            host = 'localhost',
            db = 'weixing',
            port = 3306,
            user = 'root',
            passwd = 'dxyna.',
            charset = 'utf8',
            use_unicode = False,
        )
        print('连接成功')
        # 通过cursor执行增删改查
        self.cursor = self.connect.cursor()
    def process_item(self):

        try:
            # 检测数据是否已存在
            sql = 'select * from tag where blank_name="%s" and wx_name="%s" and  title="%s" and content="%s" and urls="%s"'%(self.blank_name,self.wx_name,self.title,self.connect,self.tit_urls)
            self.cursor.execute(sql)
            repetition = self.cursor.fetchone()
            if repetition:
                print('数据已存在')
            else:
                # 插入数据
                print('正在插入')
                sql = 'insert into tag(blank_name,wx_name,title,content,urls) values (%s,%s,%s,%s,%s)'
                self.cursor.execute(sql,(self.blank_name,self.wx_name,self.title,self.connect,self.tit_urls))
                self.connect.commit()
                print('插入成功')

        except Exception:
            print('插入数据错误')

if __name__ == '__main__':
    dw = Downloader()
    # dw.get_blank_url() # 得到所有需要抓取的公众号连接
    # blank_url='https://mp.weixin.qq.com/profile?src=3&timestamp=1530005869&ver=1&signature=q5TnqplxAJO6Afw3pQEHFy5DttEoLazjeQe8HBJMoM2guRedrjjfR*zHjDrQ8BU9FFR*WMCAYc452yuMc*MIDw=='
    dw.get_title_url() # 得到公众号的所有文章链接
    for i in dw.tit_urls:
        dw.get_content(i) # 获取每一个文章的内容
