# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class KgcTwoPipeline(object):
    def process_item(self, item, spider):
        return item
# class FirstDemoPip(object):
#     '''当蜘蛛开启工作的时候调用: 打开一个文件写入对象'''
#
#     def open_spider(self, spider):
#         self.file = open('kgcExer.txt', 'wb+')
#     '''当蜘蛛开启工作的时候调用:关闭文件的调用'''
#
#     def close_spider(self, spider):
#         self.file.close()
#
#     '''当制作解析出item 把item的信息写入到file'''
#     def process_item(self, item, spider):
#         self.file.write(item['name'].encode())
#         self.file.write('.'.encode())
#         self.file.write(item['job'].encode())
#         self.file.write('\n'.encode())
