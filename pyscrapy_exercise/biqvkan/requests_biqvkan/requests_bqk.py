# 下载笔趣看小说,单线程
import sys
import requests
from bs4 import BeautifulSoup
class DownLoader(object):
    def __init__(self):
        self.url = 'http://www.biqukan.com'
        self.bookname = '/1_1094/'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebK'
                           'it/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
        }
        self.list_main_urls = []    # 章节rul
        self.list_show_names = []   # 章节标题
        self.num = 0
    def get_list_urls(self):
        '''获取章节url'''
        url = self.url+self.bookname
        response = requests.get(url=url,headers=self.header)
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        show_index = soup.find_all('dd')[12:]   # 对章节进行筛选
        self.num = len(show_index)
        for i in show_index:
            href = self.url+i.a.attrs['href']
            name = i.a.text
            self.list_main_urls.append(href)
            self.list_show_names.append(name)
    def get_show_text(self,url):
        '''获取章节内容'''
        response = requests.get(url=url,headers=self.header)
        html = response.text
        soup = BeautifulSoup(html,'lxml')
        text = soup.find('div',class_='showtxt').text
        return text
    def writer_show(self,show_name,text):
        '''将书写入文件'''
        with open('一年永恒.txt','a',encoding='utf-8') as f:
            f.write(show_name+'\n')
            f.writelines(text)
            f.write('\n\n')
if __name__ == '__main__':
    dw = DownLoader()
    dw.get_list_urls()
    for i in range(dw.num):
        text = dw.get_show_text(dw.list_main_urls[i])
        dw.writer_show(dw.list_show_names[i],text)
        sys.stdout.write("已下载：%.3f" % float(i / dw.num) + '\r')
        sys.stdout.flush()
    print('下载完成')