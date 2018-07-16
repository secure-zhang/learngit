# # 通过requests模块和正则表达式爬取猫眼电影top100
# # 流程框架  1.抓取单页内容2.正则表达式分析3.保存至文件4.开始循环
from threading import Thread

import requests,re,json
from requests.exceptions import RequestException    # 异常处理
from multiprocessing import Pool    # 进程池
def get_one_page(url):
    '''获取第一页'''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
        }
        response = requests.get(url=url,headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None
def pase_one_page(html):
    '''解析第一页,获取数据'''
    res = '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?alt="(.*?)".*?class="star">(.*?)</p>.*?class="releasetime">(.*?)</p>.*?</dd>'
    pattern = re.compile(res,re.S)
    items = re.findall(pattern=pattern,string=html)
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
    '''调用'''
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in pase_one_page(html):
        print(item)
        write_to_file(item)
    print(offset)
if __name__ == '__main__':
    # 普通写入
    # for i in range(10):
    #     main(i*10)

    # 多线程写入
    a = range(10)
    thread_list = (Thread(target=main,args=(offset*10)) for offset in a)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


