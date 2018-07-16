# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KgcDemoPipeline(object):
    def process_item(self, item, spider):
        return item
class FirstDemoPipline(object):
    def open_spider(self, spider):
        '''当蜘蛛开启工作的时候调用: 打开一个文件写入对象'''
        self.file = open('kgc.txt', 'wb+')

    def close_spider(self, spider):
        '''当蜘蛛开启工作的时候调用:关闭文件的调用'''
        self.file.close()

    def process_item(self, item, spider):
        '''当制作解析出item 把item的信息写入到file'''
        self.file.write(item['name'].encode())
        self.file.write('.'.encode())
        self.file.write(item['job'].encode())
        self.file.write('\n'.encode())
import pymysql
class DbPipline(object):
    def open_spider(self, spider):
        '''当蜘蛛开启工作的时候调用: 打开一个文件写入对象'''
        self.db = pymysql.connect(host='localhost',port=3306,user='root',passwd='dxyna.',db='kgc',charset='utf8')

    def close_spider(self, spider):
        '''当蜘蛛开启工作的时候调用:关闭文件的调用'''
        self.db.close()
    def process_item(self, item, spider):
        '''当制作解析出item 把item的信息写入到file'''
        price = item['prices'][1:]
        print('*'*80)
        if price == '费':
                price = 0
        print(int(price))
        cursor = self.db.cursor('insert into keke(name,people,price) values ({},{},{})'.format(item['name'], int(item['peoples']),float(price)))
        self.db.commit()
