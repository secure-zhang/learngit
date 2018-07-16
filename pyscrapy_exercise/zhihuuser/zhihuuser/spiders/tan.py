# # import datetime
# # now_time = datetime.datetime.now()
# # yes_time = now_time + datetime.timedelta(days=-1)
# #
# # yes_time2=datetime.datetime.now() - datetime.timedelta(days=1)
# #
# # yes_time_yes = yes_time.strftime('%Y-%m-%d %H:%M:%S')#格式化输出
# # print(now_time-datetime.timedelta(days=1))
# # print(yes_time)
# # print(yes_time2)
# # # print(yes_time_yes)
# #
# # list1 = [1,2,3,4,5,3,2,4]
# # list2 = {}
# # for i in list1:
# #     if i in list2:
# #         list2[i] +=1
# #     else:
# #         list2[i] = 1
# # print(list2)
#
# # import time
# #
# # start = time.clock()
# #
# # #当中是你的程序
# # 装饰器
# # elapsed = (time.clock() - start)
# # print("Time used:",elapsed)
#
# import time
#
# # def count_time(func):
# #     def times(*args,**kwargs):
# #         start_time = time.time()
# #         func()
# #         end_time = time.time()
# #         print((end_time-start_time),'时间差')
# #     return times
# #
# #
# # @count_time()
# # def main():
# #     print('>>>>开始计算函数运行时间')
# #     # for i in range(1, 1000):# 可以是任意函数  ， 这里故意模拟函数的运行时间
# #     #     for j in range(i):
# #     #         print(j)
# # main()
# # def zsq(flag):
# #     def zsq2(func):
# #         def qqq(*args,**kwargs):
# #             print(flag)
# #             func()
# #             print('dsa')
# #         return qqq
# #     return zsq2
# # @zsq('asd')
# # def main():
# #     print('main')
# #
# # main()
#
#
# # 单例模式
# # class Myclass1(object):
# #     _instance = None
# #     def __new__(cls, *args, **kwargs):
# #         if not cls._instance:
# #             cls._instance = super(Myclass1,cls).__new__(cls,*args,**kwargs)
# #         return cls._instance
# # class Herclass(Myclass1):
# #     a = 1
# # one = Herclass()
# # two = Herclass()
# # print(id(one),id(two))
#
# # class Myclass(object):
# #     _index = None
# #     def __new__(cls, *args, **kwargs):
# #         if not cls._index:
# #             cls._index=super(Myclass,cls).__new__(cls,*args,**kwargs)
# # class My:
# #     def __init__(self):
# #         print('init')
# #     def __new__(cls, *args, **kwargs):
# #         print('new')
# #         # return super().__new__(cls,*args,**kwargs)
# # My()
# # for i in range(5,0,-1):
# #       print(i)
# # import datetime
# # def dayofyear():
# #     year = input("请输入年份：")
# #     month = input("请输入月份：")
# #     day = input("请输入天：")
# #     date1 = datetime.date(year=int(year),month=int(month),day=int(day))
# #     print(date1)
# #     date2 = datetime.date(year=int(year),month=1,day=1)
# #     print(date2)
# #     return (date1 -date2).days
# # # print(dayofyear(),'===')
# # dict_str = "k:1|k1:2|k2:3|k3:4"
# # list_str = dict_str.split('|')
# # dict_tor = {}
# # for i in list_str:
# #       k,v = i.split(':')
# #       dict_tor[k]=v
# #
# #
# # print(dict_tor)
#
#
#
# #
# # a  = [ '1','3']
# # print(a.index('3'))
# #
# # print('*'.center(10))
#
#
# class TestCls():
#     """docstring for TestCls"""
#
#     def __init__(self, name):
#         print('init')
#         print(self)
#         print(type(self))
#         self.name = name
#
#     def __new__(cls, name):
#         print('new')
#         print(cls)
#         print(type(cls))
#         return super().__new__(cls)
#
# c = TestCls("CooMark")
#
# a = [1,2,3,4]
# b = []
# for i in a:
#     for j in a:
#         for k in a:
#             if i != k and k != j and i!=j:
#                 b.append('{}{}{}'.format(i, j, k))
# print(len(b))
# print(b)
# print(len(set(b)))
# a = ' asd \n123'
# print(a.strip())

import random

def caishuzi():
    a = random.randint(1, 100)
    print('开始游戏')
    while 1:
        one = input('请输入')
        if one.isdigit():
            one  = int(one)
            if one > a:
                print('大了')
            elif one == a:
                print('猜对了就是{}'.format(a))
                break
            else:
                print('小了')
        else:
            print('请输入数字')
# str = '我的天你好哈哈,你好'
# import re
# print(re.findall('你好',str))
# def abc(list):
#     # 先序
#     print()
# abc([1,2,3,4,5,6,7])

#
# def getAvg(l):
#     list1 = l.strip('*').split('*')
#     list2 = []
#
#     for i in list1:
#         if i.isdigit():
#             if int(i)>0:
#                 list2.append(int(i))
#     if len(list2)>0:
#         return sum(list2)/len(list2)
#
#
# with open('asd','r',encoding='utf-8') as f:
#     count = 0
#     while 1:
#         a = f.readline()
#         count+=1
#         if a:
#             print('第{}组数据平均数为'.format(count),getAvg(a))
#         else:
#             break

# 判断回文
# def huiwen(str):
#     if len(str)%2==0:
#         if str[0:len(str)//2] == str[:len(str)//2-1:-1]:
#             print('回文')
#     if len(str)%2!=0:
#         if str[0:len(str)//2] == str[:len(str)//2:-1]:
#             print('回文')
# huiwen('asdsdsa')
# #
#
# def daxiao(x,y,z):
#     if x>y :
#         if y>z:
#             print(x,y,z)
#         else:
#             print(x,z,y)
#     else:
# a = {'nba':1}
# if a:
#     print(1)
# else:
#     print(2)

# while True:
#     pass
# a = [1,2,3]
# b = [3,2,4]
# print(set(a) & set(b))
# try:
#     a = 1
# except:
#     print(1)
# f = lambda x,y:x*y
# print(f(1,34))
# x = 0
# a = [x if x else print(x),x]
# def a(a,b,c):
#     print(a+b)
# dd = (1,2,3)
# a(*dd)

# print(type({}))
a = {}
b = {1:3}
c = dict(([2,3],[4,5]))
print(a,b,c)

d=dict(((1,2),(3,4)))
print(d)
print([4 for i in range(3)])
print([1,2]+[3])
print((1,)+(2,))
print(isinstance(123,str))
a = {(2,):2}
print(a)
print(eval('2*1+1'))