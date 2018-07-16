import re

import logging
from threading import Thread
import datetime
from requests_html import HTMLSession  # 进程池
import os
from multiprocessing.pool import Pool
logging.basicConfig(level=logging.DEBUG) #配置日志
url = 'http://www.win4000.com/zt/xinggan_{}.html'
path = 'download_imgs2'
img_name_url = []
session = HTMLSession()
img_del_re = re.compile('_\d{3}_\d{2}')
def hand_girl(href,store_path):
    # 将href下面的图片放到目录中
    page = session.get(href)
    img_tags = page.html.find('.scroll-img li img')
    for i in img_tags:
        img_src = i.attrs['data-original']
        img_src = img_del_re.sub('',img_src)
        # 生成保存文件的名称, 获取链接对应的图片数据,然后保存
        file_name = img_src.split('/')[-1] # 图片的名字
        file_name = os.path.join(store_path,file_name)
        img_name_url.append((img_src,file_name))
def store_img(img_src,file_name):
    # 将图片保存
    img_data = session.get(img_src).content
    with open(file_name,'wb') as f:
        logging.debug('download..%s'%file_name)
        f.write(img_data)
    print(datetime.datetime.now())


def hand_page(page):
    # 遍历获取美女主页连接以及美女名称
    href_tags = page.html.find('.Left_list_cont .tab_box ul li a')
    for href_tag in href_tags:
        title,href = href_tag.attrs['title'],href_tag.attrs['href']
        # 创建文件夹,然后去链接将图片下载
        store_path = os.path.join(path,title)
        os.makedirs(store_path,exist_ok=True) # 支持递归创建 mkdir只创建一层 exist_ok 如果存在不报错
        hand_girl(href,store_path)

def main():
    # 怎么遍历动态变化的页数
    for i in range(1,2):
        try:
            page = session.get(url.format(2))
            hand_page(page)
        except ConnectionError:
            break

if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()

    # 线程

    thread_list = (Thread(target=store_img,args=(img_name,img_url)) for img_name,img_url in img_name_url)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
    # 线程
    # pool = Pool(4)
    # for img_src,file_name in img_name_url:
    #     # print(img_src,file_name)
    #     pool.apply_async(store_img,args=(img_src,file_name))
    # pool.close() # 关闭,会等待进程结束
    # pool.join() # 等待
    print('用时%s'%(datetime.datetime.now()-start_time))
