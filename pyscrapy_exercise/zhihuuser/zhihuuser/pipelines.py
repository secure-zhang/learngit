# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

from zhihuuser import settings
import pymysql
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
            print(item['id'])
            if item['id']:
                # select = 'select * from zhihu where zid="%s" and name="%s" and url_token="%s" and avatar_url="%s" and headline="%s"'%(item['id'],item['name'],item['url_token'],item['avatar_url'], item['headline'])
                select = 'select * from zhihu where zid="%s"'%(item['id'])
                self.cursor.execute(select)
                repetition = self.cursor.fetchone()
                if repetition:
                    print('数据已存在')
                else:
                    # 插入数据
                    print('正在插入')
                    sql = 'insert into zhihu(zid,name,url_token,avatar_url,headline) values (%s,%s,%s,%s,%s)'
                    self.cursor.execute(sql,(item['id'],item['name'],item['url_token'],item['avatar_url'], item['headline']))
                    self.connect.commit()
                    print('插入成功')

        except Exception:
            print('插入数据错误')
        return item
