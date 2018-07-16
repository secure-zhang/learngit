# coding:utf-8

# https://www.cnblogs.com/jiaoyu121/p/6944398.html 学习连接
import re

import itchat

itchat.auto_login(hotReload=True) # 登录

friends = itchat.get_friends(update=True) # 获取好友信息

tList = []
for i in friends:
    Signature = i['Signature'].strip()
    # 通过正则对数据进行清洗
    rep = re.compile('<span class="emoji |">|</span>')
    signature = rep.sub('',Signature)
    tList.append(signature)

# 拼接字符串
text = ''.join(tList)

# 结巴分词
import jieba

wordlist_jieba = jieba.cut(text,cut_all=True) # 设置词语
wl_space_split = ' '.join(wordlist_jieba)# 将字符串进行分词

# wordcloud词云

import