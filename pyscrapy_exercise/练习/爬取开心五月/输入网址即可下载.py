import os
import shutil

import requests,re
from bs4 import BeautifulSoup
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'}
def get_html(url):
    ''' 获取 页面 内容'''
    html = requests.get(url=url,headers=headers).content
    html = html.decode('gbk')
    return html
def get_soup(url):
    ''' 使用 bs4 生成soup'''
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    return soup
def parse_title(url):
    soup = get_soup(url)
    two_url = soup.find('div',{'class':'l'}).a.attrs['href']
    return two_url
def parse_content(url):
    '''获取.mp4文件的url地址'''
    two_url = parse_title(url)
    two_url = 'http://www.75bo.info'+two_url
    soup = get_soup(url=two_url)
    title = soup.find(class_='m_T2').text[:-15]
    video = soup.find(id='a1')
    video_url = re.search("f:'(.*?)',",str(video)).group(1)
    return video_url,title
def write_file(url,title):
    print('开始下载{}...'.format(title))
    content = requests.get(url=url,headers=headers).content
    with open('%s.mp4'%title,'wb') as f:
        f.write(content)
        print('下载完成!')



if __name__ == '__main__':
    while 1:
        url = input('请输入链接>>>').strip()
        if not url:
            break
        video_url, title = parse_content(url)
        write_file(url=video_url, title=title)
    print('程序退出')
