import requests
from bs4 import BeautifulSoup
import os,time,shutil
import random


def userAgent():
    user_agent_list = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"]
    return random.choice(user_agent_list)

headers = userAgent()
def get_one_page(url):
    response = requests.get(url=url,headers=headers).content
    response = response.decode('gbk')
    return response
def get_soup(url):
    '''将原先代码包装称soup对象'''
    html = get_one_page(url)
    soup = BeautifulSoup(html,'lxml')
    return soup
def get_image_list(start_url):
    # 第一个列表 list 标题
    dir_list = []
    # 第二个列表 链接
    url_list = []
    soup = get_soup(start_url)
    dd_a = soup.find('dl',{'class':'list-left public-box'}).find_all('a',{'target':'_blank'})
    for i in dd_a:
        dir_name = i.text
        urls = i.attrs['href']
        dir_list.append(dir_name)
        url_list.append(urls)
    return dir_list,url_list
def get_max_page(url):
    # 每个标题中的图片数
    html = get_one_page(url)
    soup = BeautifulSoup(html,'lxml')
    max_imgs = soup.find('div',{'class':'content-page'}).span.text[1:-1]
    return max_imgs
def down_image(start_url):
    # 完成保存图片路径的问题
    base_dir = os.getcwd()
    # 获取之前的俩个列表
    dir_list,url_list= get_image_list(start_url)
    # 将俩个列表组合压缩
    for dir_name,url in zip(dir_list,url_list):
        # 拿到每一个美女的目录名称,二级url
        if os.path.exists('%s/%s'%(base_dir,dir_name)):
            # 检测目录是否存在
            print('%s目录已经存在,先删除该目录'%dir_name)
            shutil.rmtree(dir_name)
        os.mkdir('%s/%s'%(base_dir,dir_name))  # 创建目录
        # # # 获取每个美女图片数目
        max_page = get_max_page(url)
        print('开始下载{}共{}个图片'.format(dir_name,max_page))
        # 获取每一个二级页面
        soup = get_soup(url)
        img_src = soup.find('div',{'class':'content-pic'}).img.attrs['src']
        # 获取每一张图片的共同特点
        base_url = img_src[:-5]
        for i in range(1,int(max_page)+1):
            url = base_url+str(i)+'.jpg'
            get_image(url,dir_name,i)
        print('下载完毕!')
def get_image(url,dir_name,max_page):
    content = requests.get(url=url,headers=headers).content
    with open('%s/%s.jpg'%(dir_name,max_page),'wb') as f:
        f.write(content)
def get_tag(url):
    '''选择性抓取'''
    soup = get_soup(url)
    max_page = soup.find('div',{'class':'content-page'}).span.text[1:-1]
    dir_name = soup.h5.string
    img_src = soup.find('div', {'class': 'content-pic'}).img.attrs['src']
    # 获取每一张图片的共同特点
    base_url = img_src[:-5]
    base_dir = os.getcwd()
    if os.path.exists('%s/%s' % (base_dir, dir_name)):
        # 检测目录是否存在
        print('%s目录已经存在,先删除该目录' % dir_name)
        shutil.rmtree(dir_name)
    os.mkdir('%s/%s' % (base_dir, dir_name))  # 创建目录
    print('开始下载{}共{}个图片'.format(dir_name, max_page))
    for i in range(1,int(max_page)):
        url = base_url + str(i) + '.jpg'
        get_image(url, dir_name, i)
    print('下载完毕!')


if __name__ == '__main__':
    try:
        print('请从该网站中选择:http://www.mm131.com/'.center(80,' '))
        print('请选择下载类型'.center(20,' '))
        print('1----分类下载'.center(30,' '))
        print('2----选择性下载'.center(30,' '))
        tag = input('请输入1/2>>>')
        if tag == '1':
            print('请选择分类')
            index_list = [
                ['性感美女', 'xinggan'],
                [ '清纯美眉', 'qingchun'],
                [ '美女校花', 'xiaohua'],
                [ '性感车模', 'chemo'],
                [ '旗袍美女', 'qipao'],
                [ '明星写真', 'mingxing'],
            ]
            for i in range(len(index_list)):
                print('{}----{}'.format(i,index_list[i][0]))
            index = input('>>>')
            if str(int(index)+1) in ['1','2','3','4','5','6']:
                keyword = index_list[int(index)][1]
                start_url = 'http://www.mm131.com/{keyword}/'.format(keyword=keyword)
                down_image(start_url)
        elif tag == '2':
            print('请输入链接,例如:http://www.mm131.com/qipao/1921.html')
            url = input('>>>').strip()
            get_tag(url)
        else:
            print('输入错误,程序退出')
    except:
        print('程序异常')
