import requests
def getResponse():
    response = requests.get('http://www.baidu.com/')
    print(type(response))
    print(response.status_code) # 状态码
    print(type(response.text))
    print(response.text)        # 响应的内容
    print(response.cookies)
    print(response.content)
    print(response.headers)
def postResponse():
    response = requests.post('http://www.baidu.com/post')
    print(response.headers)
# postResponse()
# response = requests.get('http://httpbin.org/get?name=zhang&age=23')
# print(response.text)

# data = {
#     'name':'zhang',
#     'age':23,
#     'sex':'man'
# }
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.text)
# print(response.json())

# response = requests.get('https://t10.baidu.com/it/u=256667715,3914103533&fm=76')
# print(response.content)
# with open('car.jpg','wb') as f:
#     f.write(response.content)
#     f.close()

# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
#
#            }
# response = requests.get('https://www.zhihu.com/get',headers=headers)
# print(response.text)


# post请求
# data = {'name':'zhang','age':23}
# response = requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.json())
# print(response.history)
# print(response.status_code)
# print(requests.codes)

# 文件上传
# files = {'file':open('car.jpg','rb')}
# response = requests.post('http://www.baidu.com/post',files=files)
# print(response.cookies)
# for k,v in response.cookies.items():
#     print(k+'='+v)

# 会话位置  模拟登录 cookies 和 session

# requests.get('http://httpbin.org/cookies/set/number/123431') # 上传cookies
# response = requests.get('http://httpbin.org/cookies') # 获取
# print(response.text)

# s = requests.session()
# s.get('http://httpbin.org/cookies/set/number/12343')
# response = s.get('http://httpbin.org/cookies')
# print(response.text)


# response= requests.get('https://www.12306.cn',verify=False)  # 跳过证书验证 verify=False
# print(response.status_code)


# 代理设置:
# proxies = {
#     'http':'http://user:passwd@127.0.0.1:9743/',
#     # 'https':'https://127.0.0.1:9743'
# }
# response = requests.get('https://www.taobao.com',proxies=proxies)
# print(response.status_code)
# print(requests.socks)
import re
# headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
#         }
# url = 'http://maoyan.com/board/4?'
# response = requests.get(url=url,headers=headers).text
# index = ''
# res = re.search('<dl.*?board-wrapper">.*?</dl>',response,re.S).group()
#
# # res2 = re.findall('<dd>.*?board-index.*?>(\d+)</i>.*?title="(.*?)".*?</dd>',response,re.S)
# res2 = re.findall('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?alt="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</dd>',response,re.S)
# print(res2)
str = '''hello,Tom
         你好,吉米Tom
         第三方
         发送豆腐干梵蒂冈风格你好您好您不好
         反对广泛的
         '''
com = '[H,h]ello|[H,h]i|[你,您]好'
res = re.findall(com,str)
print(res)
