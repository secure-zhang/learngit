# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

from exercise import settings
import pymysql
class ExercisePipeline(object):
    '''判断长度'''
    def __init__(self):
        self.limit = 50
    def process_item(self, item, spider):
        print('修改数据')
        if item['text']:
            if len(item['text']) > self.limit:
                item['text'] = item['text'][0:self.limit].rstrip()+'...'
                return item
        else:
            return DropItem('missing text')

class MysqlPip(object):
    def __init__(self,):
        # 连接数据库
        print('连接数据库')
        self.connect = pymysql.connect(
            host = settings.MYSQL_HOST,
            db = settings.MYSQL_DBNAME,
            port = 3306,
            user = settings.MYSQL_USER,
            passwd = settings.MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = False,
        )
        print('连接成功')
        # 通过cursor执行增删改查
        self.cursor = self.connect.cursor()
    def process_item(self,item,spider):

        try:
            # 检测数据是否已存在
            select = 'select * from quotes where tests="%s" and author="%s" and tags="%s"'%(item['text'],item['author'], item['tags'])
            self.cursor.execute(select)
            repetition = self.cursor.fetchone()
            if repetition:
                print('数据已存在')
            else:
                # 插入数据
                print('正在插入')
                sql = 'insert into quotes(tests,author,tags) values (%s,%s,%s)'
                self.cursor.execute(sql,(item['text'],item['author'],item['tags']))
                self.connect.commit()
                print('插入成功')

        except Exception:
            print('插入数据错误')
        return item
