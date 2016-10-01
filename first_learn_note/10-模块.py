#coding=utf-8
#第十章:模块,自带的模块称为标准库

import math
print math.sin(30)
# -0.988031624093

print '任何python程序都可以作为模块导入'
print '在模块中定义函数'
#导入hello.py模块

import hello
hello.hello()  #调用方法,模块.函数
#Hello,World! again


#为了代码可以重用，定义模块
#在模块中测试代码，在其他代码中执行hello函数，测试代码会被执行
#就是不用上面的调用hello.hello()，只要导入后，执行就会被运行


#包
#为了组织好模块，可以将他们分为包。包基本上就是另外一类模块，她们可以包含其他模块

#怎么探究模块，标准库都已经有很多了
#使用dir
#_all_变量
#使用help获取帮助

print '文档,最好的就是看doc文档，python.org/doc'
print range.__doc__

#range(stop) -> list of integers
#range(start, stop[, step]) -> list of integers

#Return a list containing an arithmetic progression of integers.
#range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0.
#When step is given, it specifies the increment (or decrement).
#For example, range(4) returns [0, 1, 2, 3].  The end point is omitted!
#These are exactly the valid indices for a list of 4 elements.

#阅读源代码，要了解模块，最好的就是阅读源代码，是学习python的最好方式

#标准库：一些最爱
#sys：可以访问与python解释器密切相关的变量和函数

#os:提供了访问多个系统服务的功能

# fileinput:轻松遍历文本文件的所有行
# fileinput模块中重要的函数
# input(files[,inplace[,backup]])    遍历多个输入流中的行
# filename()     返回当前文件的名称
# lineno()    返回当前累计行数
# filelineno()   返回当前文件行数
# isfirstline()      检查当前是否是文件的第一行
# isstdin()      检查最后一行是否来自sys.stdin
# nextfile()    关闭当前文件，移动到下一行
# close()       关闭序列

#调用
#fileinput.filename 返回当前正在处理的文件名

#集合，堆和双端队列
#集合Set
print '*********1**********'
print set(range(10))
#set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


#集合是由序列构建的，集合元素的顺序是随意的
a = set([1,2,3])
b = set([2,3,4,5])
print a.union(b)
print a|b
# set([1, 2, 3, 4, 5])
# set([1, 2, 3, 4, 5])

#.....其他的方法

#堆，优先队列的一种，
#双端队列，需要按照元素的增加顺序来移除元素

#time模块:获得当前时间，操作时间和日期，从字符串读取时间及格式化时间为字符串
#time模块中重要函数:
#asctime([tuple])  将时间元组转换为字符串
#localtime([secs])  将秒数转换为日期元组
#time()

#random模块，包括返回随机数的函数
#random模块中的重要函数
#random() 返回0<n=<1之间的随机数n

#re模块,包含对正则表达式的支持
print '学习的关键是每次只学习一点，然后使用，慢慢扩展，想要一次全部记住不现实'

#通配符，可以匹配任何字符串
#对特殊字符进行转义----前面加上反斜线 \
#   例如要匹配 python.org 因为. 所以使用 python\\.org
#字符集，[py]thon,[a-zA-Z0-9]

#re模块的内容:
import re
#re.compile(pattern[,flags]) 将正则表达式转换为模式对象,可以更加有效率的匹配

#re.search(pattern,string[,flags])  在给定的字符串中寻找第一个匹配给定正则表达式的子字符串
#   找到匹配的字符串，返回MatchObject--值为true，否则返回None--值为Flase
#   利用返回值的特点，用在if中
#   if re.search(pat,string):
#       print 'found it'

#re.match(pattern,string[,flags])  在给定字符串的开头匹配正则表达式
#   match('p','python')返回真
#   re.match('p','www.python.org')返回None

#re.split(pattern,string[,maxsplit=0])  根据模式的匹配项来匹配字符串
sometxt = 'alpha,beat...,detla'
print re.split('[,]+',sometxt)
print re.split('[,]+',sometxt,maxsplit=1)
#['alpha', 'beat...', 'detla']
#['alpha', 'beat...,detla']

#re.findall(pattern,string)
pat = '[a-zA-Z]+'        #查找对应的单词
text = '"a boy,a girl.they will be together"...it is true!!!zzk'
print re.findall(pat,text)
#['a', 'boy', 'a', 'girl', 'they', 'will', 'be', 'together', 'it', 'is', 'true', 'zzk']
pat = r'[.?\-",!]+'
print re.findall(pat,text)
#['"', ',', '.', '"...', '!!!']

#re.sub 使用给定的替换内容将匹配模式的字符串(最左端且非重叠模式的子字符串)替换掉
pat = '{name}'
text = 'Dear {name}...'
print re.sub(pat,'ZZK',text)
#Dear ZZK...

#re.escape() 将字符串中所有可能被解释为正则表达式的字符进行转义
print re.escape('www.python.org')
#www\.python\.org






























































