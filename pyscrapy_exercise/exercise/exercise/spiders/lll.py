# # # a = list('1234567890123456')
# # # print(a)
# # # b = []
# # # count = 0
# # # while 1:
# # #     if a:
# # #         count+=1
# # #         b.append(a.pop())
# # #         if count == 3:
# # #             b.append(',')
# # #             count = 0
# # #     else:
# # #         break
# # # print(''.join(b))
# # import pymysql
# # class MysqlPip(object):
# #     def __init__(self,):
# #         # 连接数据库
# #         print('连接数据库')
# #         self.connect = pymysql.connect(
# #             host = 'localhost',
# #             db = 'kgc',
# #             port = 3306,
# #             user = 'root',
# #             passwd = 'dxyna.',
# #             charset = 'utf8',
# #             use_unicode = False,
# #         )
# #         print('连接成功')
# #         # 获取光标
# #         self.cursor = self.connect.cursor()
# #
# #     def process_item(self):
# #
# #             try:
# #                 # 插入数据
# #                 print('正在插入')
# #                 sql = 'insert into quotes(tests,author,tags) values ({}{}{})'.format('a','b','c')
# #                 self.cursor.execute(sql)
# #                 self.connect.commit()
# #                 print('插入成功')
# #
# #             except Exception:
# #                 print('插入数据错误')
# # mysql = MysqlPip()
# # mysql.process_item()
# import pymysql
#
# # 连接MySQL数据库，  本机         用户名   密码      数据库名
# db = pymysql.connect('localhost', 'root', 'dxyna.', 'kgc')
# # 获取光标
# cursor = db.cursor()
# try:
#     a = cursor.execute("select * from quotes where tests='354'")
#     print(a)
#     repetition = cursor.fetchone()
#     print(repetition)
#     # sql = "insert into quotes VALUES ({},{},{})".format('354', '4566', '54654')
#     # cursor.execute(sql)
#     # 提交到数据库中去执行
#     print('正在插入')
#     # db.commit()
#     print('提交成功')
# except:
#     print('-------------')
#     # 回滚（返回原来的状况）
#     db.rollback()
# db.close()