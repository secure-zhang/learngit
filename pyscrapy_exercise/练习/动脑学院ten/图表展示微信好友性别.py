import itchat
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True) # 获取好友列表
# print(friends)
male = female = other = 0 # 初始化计步器,有男有女还有不填的

for i in friends[1:]: # 第一个是自己
    sex = i['Sex']
    if sex == 1:
        male+=1 # 男
    elif sex == 2:
        female+=1 # 女
    else:
        other+=1 # 未填写

total = len(friends[1:]) # 好友总数

# print('男性好友:%.2f%%'%(float(male)/total*100))
# print('女性好友:%.2f%%'%(float(female)/total*100))
# print('其他:%.2f%%'%(float(other)/total*100))

# 展示比例使用百分百圆饼表
from echarts import Echart,Legend,Pie

chart= Echart(u'%s的微信好友性别比例'%friends[0]['NickName'],'from Wechat') # 第一个参数为标题 第二个为解释(签名))
chart.use(Pie(
    'WeChat',
    [
        {'value':male,'name':u'男性%.2f%%'%(float(male)/total*100)},
        {'value':female,'name':u'女性%.2f%%'%(float(female)/total*100)},
        {'value':other,'name':u'其他%.2f%%'%(float(other)/total*100)},
    ],
    radius = ['50%','70%'] # 图形的大小
))

chart.use(Legend(['male','female','other']))

del chart.json['xAxis']
del chart.json['yAxis']
chart.plot() # 执行,生成文件