# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from kafka import KafkaProducer
import json
# class ZhaopinDemoPipeline(object):
#     def open_item(self, item, spider):
#         self.producer = KafkaProducer(bootserap_servers = 'python2:9092')
#     def close_spider(self,spider):
#         self.producer.close()
#     def process_item(self,item,spider):
#         msg = json.dumps(item)
#         self.producer.send('test',msg.encode())
#         return item
class ZhaopinDemoPipeline(object):
    def open_item(self, spider):
        self.producer = KafkaProducer(bootstrap_servers = 'python2:9092')
    def close_spider(self,spider):
        self.producer.close()
    def process_item(self,item,spider):
        msg='{0},{1},{2},{3}'.format(item['job_title'],item['Company'],item['price'],item['info'])
        self.producer.send('test',msg.encode())
        return item