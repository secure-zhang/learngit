def Get():
    import urllib.request, socket, urllib.error
    try:
        responses = urllib.request.urlopen('http://httpbin.org/')
        print(responses.read().decode('utf-8'))     # 响应内容
        print(type(responses))      # 响应类型
        print(responses.status)     # 状态码
        print(responses.getheaders())# 请求头
    except urllib.error.URLError as e:
        if isinstance(e.reason,socket.timeout):
            print('time out')
        else:
            print('就是有错误')
def Post():
    '''post请求,将data发送过去'''
    import urllib.request,urllib.error,urllib.parse
    urls = 'http://www.baidu.com'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    dicc = {
        'name':'Germey'
    }
    data = urllib.parse.urlencode(dicc).encode('utf-8')
    req= urllib.request.Request(url=urls,headers=headers,data=data,method='POST')
    # req= urllib.request.Request(url=urls,headers=headers,data=data)
    resp= urllib.request.urlopen(req)
    print(resp.status)



