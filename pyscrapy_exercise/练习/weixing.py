# 获取索引页url
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
# url = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query=%E6%97%85%E6%B8%B8&ie=utf8&_sug_=n&_sug_type_='
# html = requests.get(url,headers).text
# response = BeautifulSoup(html,'lxml')
# print(response.select('.news-list2 li a'))
# with open('urls链接','a',encoding='utf-8') as f:
#     for i in response.select('.news-list2 li a'):
#         if len(i.attrs['href']) > 20:
#             print(i)
            # f.write(i.attrs['href'])
            # f.write('\n')
# url = 'http://piao.qunar.com/ticket/list.htm?keyword=%E5%B1%B1%E8%A5%BF&region=&from=mpl_search_suggest&page=16'
# html = requests.get(url,headers).text
# sorp = BeautifulSoup(html,'lxml')
# lists = sorp.find_all(class_='sight_item')
# for i in lists:
#     print(i.find(class_='sight_item_price').em.string)

keyword_list = ['北京','山西','天津','上海']
print('旅游景点抓取'.center(60,'*'))
for i in range(len(keyword_list)):
    print('{}------{}'.format(i,keyword_list[i]).center(60))
start = input('选择需要抓取景点的地区,请输入序号>>>')