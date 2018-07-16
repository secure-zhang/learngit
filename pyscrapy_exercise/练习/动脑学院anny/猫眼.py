import requests
from urllib import request

import re,json,logging
from multiprocessing import Pool
# 加日志
logging.basicConfig(level=logging.DEBUG)

# 获取页面
def get_html(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'
    }
    urllibs = request.Request(url=url,headers=headers) #
    html = request.urlopen(urllibs).read() # 打开网址获取源代码
    return html.decode('utf-8')
def parse_one_page(html):
    # pattern = re.compile('<dd>.*?>(.*?)</i>.*?board-img.*?src="(.*?)".*?class="star">(.*?)<.*?releasetime">(.*?)<',re.S)
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?alt="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'imgs':item[1],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'times':item[4].strip()[5:]
        }
def write_to_file(content):
    '''写入文件'''
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')# 写入文件显示为utf-8
        f.close()
def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_html(url)
    content = parse_one_page(html)
    for item in content:
        print(item)
        write_to_file(item)
if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
    pool.close() # 关闭,会等待进程结束
    pool.join() # 等待