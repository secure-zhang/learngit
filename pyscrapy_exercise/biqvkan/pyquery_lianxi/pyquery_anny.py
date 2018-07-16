# from pyquery import PyQuery
# import requests
# # doc = PyQuery(requests.get('https://www.qiushibaike.com').text)
# # print(doc('title'))
# # f = open('','r',encoding='utf-8').read()
# # texts = PyQuery(filename='pyquery_anny.py')
# # print(texts)
#
# html = '''
# <div id="content">
# <ul class="hot">
#     <li>热搜</li>
#     <li><span>哈哈哈哈</span></li>
#     <li>连接</li>
#     <li>
#         <li>链接</li>
#     </li>
# </ul>
# </div>'''
# doc = PyQuery(str)
#
# # print(type(doc('div#content ul.hot li')))
# print(doc('li').siblings())

import re
str = 'http://www.jingyu.com/search/stack?pn=116546545'
print(re.match('.*?(\d.*)',str).group(1))
print(re.search('(\d.*)',str).group(1))
print(re.findall('(\d.*)',str))








