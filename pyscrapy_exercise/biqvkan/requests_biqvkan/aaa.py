# import requests
# from bs4 import BeautifulSoup
# name_list = []
# url_list = []
# def get_listmain(url):
#     '''索引页'''
#     response = requests.get(url)
#     html = response.text
#     soup = BeautifulSoup(html,'lxml')
#     soup.prettify() # 格式化,补全代码
#     list_main = soup.find_all('dd')[12:20] # 通过截取获得第一章到最后一章的dd标签
#     # print(list_main.a.string)
#     for i in list_main:
#         url_href = i.a.attrs['href'] # 获取章节url
#         url_list.append(url_href)
#         name_list.append(i.a.string)
# def get_showtxt(url):
#     '''详情页'''
#     headers = {
#         'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
#     }
#     response = requests.get(url=url,headers=headers)
#     html = response.text
#     soup = BeautifulSoup(html,'lxml')
#     soup.prettify()
#     text = soup.find_all('div', id='content')
#     text = text[0].text.replace('\xa0'*8, '\n\n')
#     return text
# def writes(name,text):
#     with open('舅舅.txt','a', encoding='utf-8') as f:
#         f.write(str(name)+'\n')
#         f.write(str(text))
#         f.write('\n\n')
# def main(book_index):
#     '''调用接口'''
#     url = 'http://www.biqukan.com'
#     url_str = url+book_index
#     first_index = get_listmain(url=url_str)
#     for i in url_list:
#         url_show = url+i
#         text = get_showtxt(url_show)
#         # name = name_list[i]
#         # writes(name,text)
# if __name__ == '__main__':
#     # 程序主入口
#     book_index = '/1_1094/'
#     main(book_index)
#     print(name_list)
#     print(url_list)
#
#
#
