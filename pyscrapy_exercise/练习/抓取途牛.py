import random
import re
import time
from requests.exceptions import RequestException
import ip_proxy
import datetime
import requests
from bs4 import BeautifulSoup
import user_agent

headers = {'User-Agent':user_agent.userAgent()}
def get_page(url):
    # 获得分页内容
    html = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    pasre_page_url(soup)


def pasre_page_url(soup):
    # 解析分页内容获得详情页url
    try:
        page_list = soup.find(class_='thebox').find_all('li')
        for i in page_list:
            mid = i.a.attrs['m']    # 产品id
            url = 'http://'+i.a.attrs['href'].strip('/')
            get_content(url,mid)
    except:
        print('爬取完成')
def get_content(url,mid):
    '''获取详情页内容'''

    # sleep_time = [1, 2, 3, 4, 5] # 随机频率
    # time.sleep(random.choice(sleep_time))

    html = requests.get(url=url,headers=headers).text
    soup = BeautifulSoup(html,'lxml')
    parse_content(soup,mid,url)
def parse_content(soup,mid,url):
    '''解析详情页内容'''
    try:
        title = soup.find(class_='resource-title').strong.string    # 标题
        price = soup.find(class_='price-number')            # 价格
        if  price:
            price = soup.find(class_='price-number').string
        else:
            price = '暂无详情'

        people_nums = soup.find(class_='resource-people-item') # 人数
        if people_nums:
            people_nums = soup.find(class_='resource-people-item').a.string
        else:
            people_nums = '暂无详情'
        sat = soup.find(class_='resource-statisfaction-number') # 满意度
        if sat:
            satisfaction = re.search('>(.*?)<',str(sat)).group(1)  # 通过正则摘取满意度
        else:
            satisfaction = '暂无详情'
        rou = soup.find(class_='J_DetailRouteBriefInner')       # 路线
        if rou:
            route = re.sub('[ ,\n]', '', str(rou.text))
        else:
            rou = soup.find(class_='detail-journey-4-nav-list')
            route = re.sub('[ ,\n]', '', str(rou.text))
        push_mysql(mid, title, price, people_nums, satisfaction, route, url) # 写入到数据库
    except:
        print('解析内容错误')
    # file_write(title, price, people_nums, satisfaction, route) # 写入文件
def push_mysql(mid,title,price,people_nums,satisfaction,route,url):
    # 将数据保存到数据库
    mq = My_sql(mid,title,price,people_nums,satisfaction,route,url)
    mq.process_item()
nums = 0
import pymysql
class My_sql:
    def __init__(self,mid,title,price,people_nums,satisfaction,route,url):
        self.mid = mid
        self.title = title
        self.price = price
        self.people_nums = people_nums
        self.satisfaction = satisfaction
        self.url = url
        self.route = route
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
            sql = 'select * from tuniu where  mid="%s"'%(self.mid)
            self.cursor.execute(sql)
            repetition = self.cursor.fetchone()
            if repetition:
                print('数据已存在')
            else:
                # 插入数据
                sql = 'insert into tuniu(mid,title,price,people_nums,satisfaction,route,url) value (%s,%s,%s,%s,%s,%s,%s)'
                self.cursor.execute(sql,(self.mid,self.title,self.price,self.people_nums,self.satisfaction,self.route,self.url))
                self.connect.commit()
                global nums
                nums+=1
                print('正在插入{}条'.format(nums))

        except Exception:
            print('插入数据错误')

def file_write(title,price,people_nums,satisfaction,route):
    '''写入到文件'''
    with open('旅游套餐.txt','a',encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        strs = '价格:{}元,出行人数:{},满意度:{}%'.format(price,people_nums,satisfaction)
        f.write(strs)
        f.write('\n')
        f.write(route)
        f.write('\n')
        f.write('\n')
        print('写入成功')

def get_start_keyword():
    '''选择地区'''
    keyword_list = ['全国','北京', '山西', '天津', '上海','广东']
    print('旅游套餐抓取'.center(60, '*'))
    for i in range(len(keyword_list)):
        print('{}------{}'.format(i, keyword_list[i]).center(60))
    start = input('选择需要抓取套餐的地区,请输入序号>>>')
    if start.isdigit():
        if int(start)>len(keyword_list) or int(start)<0:
            print('请正确选择')
        else:
            print('正在抓取%s地区套餐...'%keyword_list[int(start)])
            return keyword_list[int(start)]
    else:
        print('请正确选择')
def main():
    count = 0
    keyword = get_start_keyword()
    while True:
        count+=1
        url = 'http://s.tuniu.com/search_complex/whole-nj-0-{keyword}/{page}'.format(keyword=keyword,page=count)
        try:
            get_page(url)
        except RequestException:
            print(RequestException)
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print('共抓取{}条数据,共用时:{}'.format(nums,end_time-start_time))