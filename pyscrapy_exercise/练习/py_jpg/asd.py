import requests
url_list = '''http://img1.mm131.me/pic/2288/1.jpg
http://img1.mm131.me/pic/2288/2.jpg
http://img1.mm131.me/pic/2288/3.jpg
http://img1.mm131.me/pic/2288/4.jpg
http://img1.mm131.me/pic/2288/5.jpg
http://img1.mm131.me/pic/2288/6.jpg
http://img1.mm131.me/pic/2288/7.jpg
http://img1.mm131.me/pic/2288/8.jpg
http://img1.mm131.me/pic/2288/9.jpg
http://img1.mm131.me/pic/2288/10.jpg
http://img1.mm131.me/pic/2288/11.jpg
http://img1.mm131.me/pic/2288/12.jpg
http://img1.mm131.me/pic/2288/13.jpg
http://img1.mm131.me/pic/2288/14.jpg
http://img1.mm131.me/pic/2288/15.jpg
http://img1.mm131.me/pic/2288/16.jpg
http://img1.mm131.me/pic/2288/17.jpg
http://img1.mm131.me/pic/2288/18.jpg
http://img1.mm131.me/pic/2288/19.jpg
http://img1.mm131.me/pic/2288/20.jpg
http://img1.mm131.me/pic/2288/21.jpg
http://img1.mm131.me/pic/2288/22.jpg
http://img1.mm131.me/pic/2288/23.jpg
http://img1.mm131.me/pic/2288/24.jpg
http://img1.mm131.me/pic/2288/25.jpg
http://img1.mm131.me/pic/2288/26.jpg
http://img1.mm131.me/pic/2288/27.jpg
http://img1.mm131.me/pic/2288/28.jpg
http://img1.mm131.me/pic/2288/29.jpg
http://img1.mm131.me/pic/2288/30.jpg
http://img1.mm131.me/pic/2288/31.jpg
http://img1.mm131.me/pic/2288/32.jpg
http://img1.mm131.me/pic/2288/33.jpg
http://img1.mm131.me/pic/2288/34.jpg
http://img1.mm131.me/pic/2288/35.jpg
http://img1.mm131.me/pic/2288/36.jpg
http://img1.mm131.me/pic/2288/37.jpg
http://img1.mm131.me/pic/2288/38.jpg
http://img1.mm131.me/pic/2288/39.jpg
http://img1.mm131.me/pic/2288/40.jpg
http://img1.mm131.me/pic/2288/41.jpg'''
url_list2 = url_list.split()

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0','Referer':'http://www.mm131.com/'}
count = 0
html = requests.get(url=url_list2[1],headers=headers).content
with open('asc/a.jpg','wb') as f:
        f.write(html)

