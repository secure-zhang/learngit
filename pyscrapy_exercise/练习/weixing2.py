import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'}
url = 'http://mp.weixin.qq.com/profile?src=3&timestamp=1530006498&ver=1&signature=q5TnqplxAJO6Afw3pQEHFy5DttEoLazjeQe8HBJMoM2guRedrjjfR*zHjDrQ8BU9LRk5XuWXxgzl-n7oiIPs7g=='
browser = webdriver.PhantomJS()
browser.get(url)
html = browser.execute_script("return document.documentElement.outerHTML")
soup = BeautifulSoup(html,'lxml')
soup = soup.find_all(class_='weui_media_bd')
str = 'http://mp.weixin.qq.com'
count = 0
with open('title_urls.txt','a',encoding='utf-8') as f:
    for i in soup:
        count+=1
        urls = i.h4.attrs['hrefs'].strip()
        title = i.h4.string.strip()
        f.write(title)
        f.write('\n')
        f.write(str+urls)
        f.write('\n')
