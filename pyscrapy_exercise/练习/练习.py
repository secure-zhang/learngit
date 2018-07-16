# # BeautifulSoup
# from bs4 import BeautifulSoup
# html = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>我的天<span>我的神</title>
# </head>
# <body>
# <p class='name'>注册成功!</p>
# <a><span>张泽睿</span><p >登录</p><p class='gime'>成功</p></a>
# {{ blogUserid.username}}----{{ blogUserid.pwd }}--{{ id }}
#
# '''
# # soup = BeautifulSoup(html,'lxml')
# # soup.prettify()  # 格式化代码,将代码补全
# # print(soup.title)   # 标签选择,如果有多个标签,它只会返回第一个内容
# # print(type(soup.title))
# # print(soup.p.attrs['class'])
# # print(soup.p['class'])
# # print(soup.a.p.string)
# # print(soup.head.contents) # 获取子节点 ,返回的是列表类型
# # for i,k in enumerate(soup.head.children):   # 获取子节点,返回的是一个迭代器
# #     print(i,k)
# # for i in soup.head.descendants:     # 获取子孙节点,返回的是一个生成器
# #     print(i)
# # print('*'*80)
# # # print(soup.p.parent)    # 获取父节点
# # # print(list(enumerate(soup.p.parents)))
# # print(list(enumerate(soup.a.p.next_siblings)))
# # print(list(enumerate(soup.a.p.previous_siblings)))
# # print('='*80)
# #标准选择器: 根据表情名,属性,内容查找文档
# html2 = '''
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <div class="main">
#     <div class="center">
#         <ul class="ullllll">
#             <li>1</li>
#             <li id='www'>2</li>
#             <li>3</li>
#             <li>4</li>
#         </ul>
#         <ul class="aaa">
#             <li>q</li>
#             <li >w</li>
#             <li>e</li>
#             <li>r</li>
#         </ul>
#     </div>
# </div>
# </body>
# </html>
# '''
# soup = BeautifulSoup(html2,'lxml')
# # div = soup.find_all('div')
# # for i in div:
# #     print(i.find_all(attrs={'class':'center'}))
# # print(soup.find_all(text='1'))
# # print(soup.find_all('li'))
# # print(soup.find('li'))
#
# # css选择器
# # for i in soup.select('ul'):
# #         print(i.get_text())
# #         print(i['class'])
# #         print(i.attrs['class'])
# from pyquery import PyQuery
# # doc = PyQuery(url='http://www.baidu.com')
# doc = PyQuery(html2)
# print(doc('.center'))
import random
import time

# sleep_time = [1,2,3,4,5]
# print(random.choice(sleep_time))
a = None
if not a:
    print('它是空 ')
    title = soup.find(class_='resource-title').strong.string    # 标题
    price = soup.find(class_='price-number').string             # 价格
    if not price:
        price = '暂无详情'
    people_nums = soup.find(class_='resource-people-item').a.string # 人数
    if not people_nums:
        people_nums = '暂无详情'
    sat = soup.find(class_='resource-statisfaction-number') # 满意度
    if sat:
        satisfaction = re.search('>(.*?)<',str(sat)).group(1)  # 通过正则摘取满意度
    else:
        satisfaction = '暂无详情'
    rou = soup.find(class_='J_DetailRouteBriefInner')       # 路线
    if not rou:
        rou = soup.find(class_='detail-journey-4-nav-list')
        print(rou)
    route = re.sub('[ \n]', '', str(rou.txt))