# 通过分析发现
# 流程框架  1.抓取索引页内容 2.抓取详情页内容 3.开启循环及多线程 4.下载图片与保存数据库
import requests,json,re
from urllib.parse import urlencode
from requests.exceptions import RequestException    # 异常处理
def headers():
    '''模拟浏览器'''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    return headers
def get_page_index(offest,keyword):
    '''抓取索引页内容'''
    data = {
        'autoload': 'truea',
        'count': 20,
        'cur_tab': 1,
        'format': 'json',
        'from':'search_tab',
        'keyword': keyword,
        'offset':offest
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    try:
        response = requests.get(url=url,headers=headers())
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print('索引页出错')
        return None
def parse_page_index(html):
    '''解析索引页,获取详情页的url'''
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            if item.get('article_url') and item.get('title'):
                yield {
                    'article_url':item.get('article_url'),
                    'title':item.get('title')
                }
            else:continue

def get_page_detail(url):
    '''抓取详情页内容'''
    try:
        response = requests.get(url=url,headers=headers())
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        print('详情页出错')
        return None
def parse_page_detail(content):
    '''解析详情页'''
    res = re.search('BASE_DATA.galleryInfo.*?title:(.*?),.*?gallery:(.*?)siblingList',content,re.S)
    if res:
        title = res.group(1)
        imgurl = re.findall('"http:.*?"',res.group(2))
        imglist = []
        for i in imgurl:
            imglist.append(re.sub(r'\\', '',i))
        yield {
            'title':title,
            'imglist':imglist
        }




def main():
    '''调用接口'''
    # for i in range(10):
    html = get_page_index(0,'街拍')
    for item in parse_page_index(html):
        '''循环抓取详情页内容,并进行解析抓取图片'''
        content = get_page_detail(item['article_url'])
        if content is not None:
            for i in parse_page_detail(content):
                print(i)

if __name__ == '__main__':
    main()