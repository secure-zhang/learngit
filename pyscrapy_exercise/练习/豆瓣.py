# 爬取豆瓣图书,通过requests和正则
import requests
import re
douban = requests.get('https://book.douban.com/').text
# print(douban)
strs = re.search('<ul.*?list-col list-col5 list-express slide-item">(.*?)</ul>',douban,re.S).group(1)
# print(strs)
str2 = re.findall('<div.*?info">.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?<div.*?author">(.*?)</div>.*?</div>',strs,re.S)
mybook = []
for i in str2:
    url,book,name=i
    name=re.sub('\s','',name)
    mybook.append({'name':name,'book':book,'url':url})
print(mybook)
