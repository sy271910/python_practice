# -*- coding: UTF-8 -

# from practice2 import python_sy #引入text的python_sy函数
# python_sy()

import cmath         #引入模块   要使用 math 或 cmath 函数必须先导入
print(dir(cmath))     #dir返回的列表容纳了在一个模块里定义的所有模块，变量和函数
print(cmath.sin(1))

import time
from datetime import datetime
localtime = time.localtime(time.time())
print("本地时间为 :",  localtime)
# 格式化时间
localtime = time.asctime( time.localtime())
print("本地时间为 :", localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
import calendar
cal = calendar.month(2018, 1)
print("以下输出2018年1月份的日历:")
print(cal)

now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))

#File
# ****************************************************打开foo.text: cat foo.txt*************
fo = open("foo.txt", "w")
fo.write("ssssyyyy")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

fo = open("foo.txt", "r+")
str = fo.read(6)
position = fo.tell() #返回当前位置
position = fo.seek(0, 0) #设置文件当前位置
print("读取的字符串是 : ", str)
fo.close()
print("是否已关闭 : ", fo.closed)

import os
# os.rename("foo.txt","foo1.txt") #重命名
# os.remove("foo1.txt")#删除
# os.mkdir("newdir")  #创建目录newdir
# os.getcwd() #返回当前的工作目录
# os.chdir("newdir")  #将当前目录改为"newdir"
# os.rmdir("newdir")  #删除目录newdir