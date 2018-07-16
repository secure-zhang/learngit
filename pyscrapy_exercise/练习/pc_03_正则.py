import re
# str = '''asdasHello 123 456 World_This
# is a Regex Demo'''
# # result = re.match('^\w+.\d+.\d+.\w{2,10}.*\w$',str)
#
# result = re.search('.ello.*?(\d+.*\d).*o',str,re.S)
# print(result)
# print(result.group(1))
# print(result.span())


str = ''' 
<p class="content">
    <a href="https://blog.csdn.net/dxyna/article/details/80098060" target="_blank">
    Apache Kafka是分布式发布-订阅消息系统,是一个消息中间件框架,是一种快速、可扩展的、设计内在就是分布式的，分区的和可复制的提交日志服务。基本框架:    它的架构包括以下组件：1、话题（Topic）：是特定类型的消息流。消息是字节的有效负载（Payload），话题是消息的分类名或种子（...      </a>
</p>
<div class="info-box d-flex align-content-center">
    <p>
        <span class="date">2018-04-26 20:38:02</span>
    </p>
    <p>
        <span class="read-num">阅读数：76</span>
    </p>
    <p>
        <span class="read-num">评论数：0</span>
    </p>
'''
res = re.sub('<span.*?>|</span>','',str)  # 通过这个方法可以删除标签
res = re.sub('<a.*?>\s.*?</a>',' ',res)
print(res)
result = re.findall('<p>\s(.*?)</p>',res,re.S)
print(result)
# content = '
# asdasds12312312sadas'
# result = re.sub('(\d+)',r'\1 231',content)
# print(result)