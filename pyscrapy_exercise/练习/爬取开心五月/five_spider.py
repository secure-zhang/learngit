import os
import re
import datetime
import requests
from bs4 import BeautifulSoup

headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; rv:61.0) Gecko/20100101 Firefox/61.0'}

def get_soup(url):
    ''' 获取 页面 内容,使用 bs4 生成soup'''
    html = requests.get(url=url,headers=headers).content
    html = html.decode('gbk')
    soup = BeautifulSoup(html,'lxml')
    return soup
def parse_main(start_url):
    # 得到分类url
    soup = get_soup(start_url)
    keyword_list = []
    ul = soup.find(class_='n_Box').find_all('li')
    for li in ul:
        keyword = li.a.attrs['href']
        keyname = li.a.text
        keyword_list.append([keyname,keyword])
    return keyword_list
def get_key_url(url):
    # 得到标题和one_url(一级url)
    soup = get_soup(url)
    title_list = []
    ul = soup.find(class_='m_Box1').find_all('li')
    for li in ul:
        title = li.find('a',{'class':'txt'}).text
        oneurl = li.find('a',{'class':'txt'}).attrs['href']
        title_list.append([title,oneurl])
    return title_list
def get_two_url(url):
    soup = get_soup(url)
    two_url = soup.find('div',{'class':'l'}).a.attrs['href']
    return two_url
def parse_content(url):
    '''获取.mp4文件的url地址'''
    two_url = get_two_url(url)
    two_url = 'http://www.75bo.info'+two_url
    soup = get_soup(url=two_url)
    video = soup.find(id='a1')
    video_url = re.search("f:'(.*?)',",str(video)).group(1)
    return video_url
def write_file(url,title):
    content = requests.get(url=url,headers=headers).content
    base_dir = os.getcwd()
    if not os.path.exists('%s' % (base_dir)):
        os.mkdir('%s/%s' % (base_dir, 'OpenMe'))  # 创建目录
    with open('%s/OpenMe/%s.mp4'%(base_dir,title),'wb') as f:
        f.write(content)
    print('文件存放在%s/OpenMe'%base_dir)

if __name__ == '__main__':
    start_url = 'http://www.75bo.info/'
    keyword_list = parse_main(start_url)
    print('拥有我就等于拥有了天下'.center(80))
    while 1:
        for i in range(1,len(keyword_list)):
            print('{}--------{}'.format(i,keyword_list[i][0]))
        tag = input('请选择>>>')
        # 获得选择的分类
        keyword = keyword_list[int(tag)][1]
        # 获得分类页面的one_url和标题
        title_list = get_key_url(url=start_url+keyword)
        print('开始时间%s将下载%s文件'%(datetime.datetime.now(),len(title_list)))
        for i in title_list:
            title = i[0]
            one_url = i[1]
            # 得到视频的地址
            print('正在下载'+title+'请耐心等候...')
            video_url = parse_content(start_url+one_url)
            write_file(url=video_url,title=title)
        tag2 = input('是否继续y/n')
        if tag2 == 'y':
            continue
        else:
            print('结束时间%s'%datetime.datetime.now())
            break

