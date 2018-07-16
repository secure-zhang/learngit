# import itchat
# from itchat.content import TEXT
# # itchat.auto_login(hotReload=True) # 缓冲登录信息
# #
# # itchat.send_msg('hello',toUserName='filehelper')
#
# # @itchat.msg_register(TEXT)  # 通过装饰起定义本函数处理什么类型的消息
# #
# # def text_replay(msg):
# #     '''接受数据'''
# #     print(msg)
# #     return msg.text
# #
# # itchat.auto_login(hotReload=True)
# # itchat.run()
#
# from itchat.content import PICTURE,VIDEO # PICTURE -- img VIDEO -- vid
# @itchat.msg_register([PICTURE,VIDEO])
# def download_file(msg):
#     '''下载图片'''
#     msg.download(msg.fileName) # 将文件放到文件名对应的文件中
#     msg_type = msg.type
#     msg_type = {PICTURE:'img',VIDEO:'vid'}.get(msg_type,'file')
#     return '@%s@%s'%(msg_type,msg.fileName)
# itchat.auto_login(hotReload=True)
# itchat.run()
#

import itchat
itchat.auto_login(hotReload=True) # 登录
itchat.send(u'你好','tan19961028') # 发送消息



