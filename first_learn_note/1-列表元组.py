#coding=utf-8

print '加油！每一个可以努力的日子都值得珍惜'

#基础知识点回顾
#列表和元组，都是序列的一种
#区别：列表可以改变，元组不能
#用序列表示数据库中一个人的信息
ed = ['zzk',22]    #这是一个列表，有两个元素
jo = ['aj',22]
database = [ed,jo]  #这里是序列包含另外一个序列
print database
# [['zzk', 22], ['aj', 22]]


#通用的序列操作
#索引
greeting = 'hello'    #序列中所有元素都有编号，从0开始递增，通过编号访问元素，这就是索引
print greeting[3]
print greeting[-1]
print 'hello'[1]
# l
# o
# e

#分片：用分片操作访问一定范围内的元素,需要提供两个索引作为边界
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]   # http://www.python.org
print tag[32:-4]   # Python web site

num = [0,1,2,3,4,5,6,7,8,9]
print num[3:6]            #这里可以看出最后的6是不包括的
print num[0:1]
# [3, 4, 5]
# [0]

#eg：对http://www.something.com形式的url进行分割
#url = raw_input('please inter the url:')
#domain = url[11:-4]
#print "Domain name:" + domain    #这里用的是 ""  后面是 + 进行拼接

#输出：
#please inter the url:http://www.baidu.com
#Domain name:baidu

#更大的步长
print num[0:10:2]
# [0, 2, 4, 6, 8]
num1 = [12,23,34,45]
print len(num1)     #对一个列表求长度 len()函数
print max(num1)     #对一个列表求最大值 max()函数
print min(num1)     #对一个列表求最小值 min()函数
# 4
# 45
# 12

#列表
#list函数，把字符串创建为列表
print list('hello')
# list = ['h', 'e', 'l', 'l', 'o']

#基本列表操作
x = [1,2,3]

x[1] = 23   #赋值
print x[1]
#23

#Author:zzk
x = [23,24]
print(x)

x[1] = 23
print(x)

del x[1]   #删除元素
print x
#[1, 3]

name = list('perl')  #分片赋值
print name
#['p', 'e', 'r', 'l']
name[2:] = list('ar')
print name
#['p', 'e', 'a', 'r']

# 列表的方法
#方法的调用，  对象.方法(参数)
tc = [1,1,2,3]   #追加，直接修改新的列表
tc.append(4)    #append方法，在列表后面追加
print tc
#[1, 1, 2, 3, 4]

print tc.count(1)  #count方法，统计某个元素在列表中出现的次数
#2

tc2 = ['tc','aj']
tc.extend(tc2)    #在列表末尾一次性追加，另外一个序列的多个值
print tc
#[1, 1, 2, 3, 4, 'tc', 'aj']

print tc.index('tc')  #index方法，从列表中返回某个值的第一个匹配项的索引位置
#5

tc.insert(1,'tc')    #insert方法，将对象插入到列表中指定索引位置
print tc
#[1, 'tc', 1, 2, 3, 4, 'tc', 'aj']

tc.pop(1)    #pop方法，将指定索引位置的元素弹出
print tc
#[1, 1, 2, 3, 4, 'tc', 'aj']

tc.remove('aj')     #删除对应的项
print tc
#[1, 1, 2, 3, 4, 'tc']

tc.reverse()       #
print tc
#['tc', 4, 3, 2, 1, 1]

tc.sort()   #sort方法，对列表进行排序
print tc
#[1, 1, 2, 3, 4, 'tc']



#元组
aa = (1,1,2,2,3)
print aa
# (1, 1, 2, 2, 3)

aa = tuple(['aa','bb','cc'])    #tuple方法，把列表转为元组
print aa
# ('aa', 'bb', 'cc')

x = 1,2,3
print x
print x[1]
print x[0:2]
#(1, 2, 3)
#2
#(1, 2)

#元组的意义
#元组可以当作键使用，列表不可以
#元组作为很多内建方法的返回值，所以必须会对元组进行处理


