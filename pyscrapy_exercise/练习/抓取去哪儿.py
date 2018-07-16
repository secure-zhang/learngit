import datetime
import random
import time

import requests
from bs4 import BeautifulSoup
import urllib.parse
import user_agent # 代理user-agent
headers = {'User-Agent':user_agent.userAgent()}
def get_view(keyword,page):
    # 获取页面
    url = 'http://piao.qunar.com/ticket/list.htm?keyword={keyword}&region=&from=mpl_search_suggest&page={page}'.format(keyword=keyword,page=page)
    html = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(html,'lxml').find(id='search-list')
    return soup
def parse_view(soup,keyword):
    # 解析页面#
    view_list = soup.find_all(class_='sight_item')
    for i in view_list:
        name = i.find(class_='name').string # 名称
        str = 'http://piao.qunar.com'
        url = str + i.find(class_='name').attrs['href']
        price = i.find(class_='sight_item_price').em.string # 价格
        address = i.find(class_='area').a.string    # 地址
        if not address:
            address = '暂无详情'
        volume = i.find(class_='hot_num').string    # 月销量
        if not volume:
            volume = '暂无详情'
        specials_move = i.find(class_='relation-subsight') # 特色
        if specials_move:
            special = []
            for i in specials_move.select('span'):
                special.append(i.string)
        else:
            special = '暂无详情'
        push_mysql(name, price, address, volume, special, url,keyword)
def push_mysql(name,price,address,volume,special,url,keyword):
    # 将数据保存到数据库
    mq = My_sql(name,price,address,volume,special,url,keyword)
    mq.process_item()

import pymysql
class My_sql:
    def __init__(self,name,price,address,volume,special,url,keyword):
        self.vname = name
        self.price = price
        self.address = address
        self.volume = volume
        self.special = str(special)
        self.url = url
        self.keyword = keyword
        # 连接数据库
        self.connect = pymysql.connect(
            host = 'localhost',
            db = 'weixing',
            port = 3306,
            user = 'root',
            passwd = 'dxyna.',
            charset = 'utf8',
            use_unicode = False,
        )
        # 通过cursor执行增删改查
        self.cursor = self.connect.cursor()
    def process_item(self):

        try:
            # 检测数据是否已存在
            sql = 'select * from qvnaer where  vname="%s"  and address="%s"  and url="%s"'%(self.vname,self.address,self.url)
            self.cursor.execute(sql)
            repetition = self.cursor.fetchone()
            if repetition:
                print('数据已存在')
            else:
                # 插入数据
                sql = 'insert into qvnaer(keyword,vname,price,address,volume,special,url) value (%s,%s,%s,%s,%s,%s,%s)'
                self.cursor.execute(sql,(self.keyword,self.vname,self.price,self.address,self.volume,self.special,self.url))
                self.connect.commit()
                print('插入数据成功')
        except Exception:
            print('插入数据错误')

def get_start_keyword():
    '''选择地区'''
    keyword_list = ['全国','北京', '山西', '天津', '上海','广东']
    print('旅游景点抓取'.center(60, '*'))
    for i in range(len(keyword_list)):
        print('{}------{}'.format(i, keyword_list[i]).center(60))
    start = input('选择需要抓取景点的地区,请输入序号>>>')
    if start.isdigit():
        if int(start)>len(keyword_list) or int(start)<0:
            print('请正确选择')
        else:
            print('正在抓取%s地区景点...'%keyword_list[int(start)])
            return keyword_list[int(start)]
    else:
        print('请正确选择')
def main():
    # 调用接口
    keyword = urllib.parse.quote(get_start_keyword()) #  获取地区
    start_time = datetime.datetime.now()
    count = 1
    while 1:
        count += 1
        soup = get_view(keyword,count) # 插入对应地区url以及分页
        if soup:
            try:
                sleep_time = [1,2,3,4,5]
                time.sleep(random.choice(sleep_time)) # 随机频率
                parse_view(soup, urllib.parse.unquote(keyword)) # 获取内容并保存到数据库
            except:
                print('第%s页之后为免费景点,暂不抓取'%count)
                print('成功抓完%s页数据,共%s条' % (count, count * 15))
                break
        else:
                # 页面不存在说明已经超过的分页数,索引
                break
    end_time = datetime.datetime.now()
    print('共用时%s'%(end_time-start_time))
if __name__ == '__main__':
    main()


