import re

import requests
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
    '''解析 页面 获得 每一个视频的标题和一级链接'''
    soup = get_soup(url)
    title_list = []
    ul = soup.find(class_='m_Box1').find_all('li')
    for li in ul:
        title = li.find('a',{'class':'txt'}).text
        oneurl = li.find('a',{'class':'txt'}).attrs['href']
        title_list.append([title,oneurl])
    return title_list

def parse_keyword(url):
    '''获取分类名字和关键url'''
    soup = get_soup(url)
    keyword_list = []
    ul = soup.find(class_='n_Box').find_all('li')
    for li in ul:
        keyword = li.a.attrs['href']
        keyname = li.a.text
        keyword_list.append([keyname,keyword])
    return keyword_list
def start_keyword():
    '''用户选择下载类型'''
    print('请从该网站中选择:http://www.75bo.info/'.center(80, ' '))
    print('请选择下载类型'.center(20, ' '))
    print('1----分类下载'.center(30, ' '))
    print('2----选择性下载'.center(30, ' '))
    tag = input('请输入1/2>>>')
    if tag == '1':
        print('请选择分类')
        url = 'http://www.75bo.info'
        keyword_list = parse_keyword(url) # 获取keyword和keyname
        for i in range(1,len(keyword_list)):
            print('{}----{}'.format(i, keyword_list[i][0]))
        index = input('>>>')
        keyword = keyword_list[int(index)][1]
        return keyword

def start_title(url):
    '''选择下载下载内容'''
    title_list = parse_title(url)
    for i in range(len(title_list)):
        print('{}---------------{}'.format(i,title_list[i][0]))
    tag = input('请选择需要下载内容(数字)>>>')
    print('您正在下载{}'.format(title_list[int(tag)][0]))
    one_url = title_list[int(tag)][1]
    print(one_url)
def parse_title_url(url):
    soup = get_soup(url)
    two_url = soup.find('div',{'class':'l'}).a.attrs['href']
    return two_url
def parse_content(url):
    '''获取.mp4文件的url地址'''
    two_url = parse_title_url(url)
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
def main():
    # 程序真实主入口
    keyword = start_keyword()
    url = 'http://www.75bo.info'+keyword
    start_title(url)


    video_url, title = parse_content(url)
    write_file(url=video_url, title=title)

if __name__ == '__main__':
    main()
    # 程序测试入口
