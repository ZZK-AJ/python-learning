#coding=utf-8
print 'day day up'

#条件和条件语句
#name = raw_input('what is your name?')
#if name.endswith('zzk'):
#    print 'hello zzk@aj'
#else:
#    print 'aj@zzk'

#elseif 语句
#num = input('enter a number:')
#if num > 0:
#    print 'the number >0'
#elif num < 0:
#    print 'the number <0'
#else:
#   print 'the number is zero'

#比较运算符
#x == y  x等于y
#.......
print 'fff' == 'fff'
#True

#in 成员资格运算符
#if name in names:
#    print '.....'

#循环
#while
#使用while打印出1~100的数字
#x = 1
#while x <= 100:
#    print x
#    x += 1

#name = ''
#while not name:            #这里使用not name ，name的值一开始为空，所以一直为
#    name = raw_input('please must input your name:')
#print 'hello,%s' %name
#只要name 的值还是 '' 空字符，就会一直要求输入

print '********************'

#for
#网易笔试题：
t = 'aj'
s = 'zzk@ajaj'
x = list(t)
print x
# ['a', 's', 'd']
num = len(t)
for i in range(num):
    if x[i] in s:
        print 'yyy'
    # # else:
    #     print 'Yes'

print '********************'

words = ['this','is','an','eg']        #遍历一个
for word in words:
    print word
# this
# is
# an
# eg

numbers = ['1','2','3','4','5']   #这里输入的为定义了的变量 num
for num in numbers:
    print num
# 1
# 2
# 3
# 4
# 5


print '********************'

#迭代--循环的另外一种说法 迭代某个范围内的数字是很常见的，可以使用内建函数 range
print range(1,10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#打印1-100数字
for i in range(5):
    print i
# 0
# 1
# 2
# 3
# 4

#使用循环遍历字典元素
d = {'x':'1','y':'2','z':'3'}
for value in d:
    print value
#输出：  可以看出，输出的是 for循环输出的是 键
#y
#x
#z

#同时迭代两个序列
names = ['zzk','aj','zzkaj']
age = ['21','22','23']
for i in range(len(names)):
    print 'names[i] is age[i]'
    print names[i], 'is', age[i], 'years old'   #这里的格式要注意,加上 ,
# names[i] is age[i]
# zzk is 21 years old
# names[i] is age[i]
# aj is 22 years old
# names[i] is age[i]
# zzkaj is 23 years old


#使用内建的zip函数，用来并行迭代，返回一个元组的列表
print zip(names,age)
# [('zzk', '21'), ('aj', '22'), ('zzkaj', '23')]

print '********************'

#按索引迭代
strings = ['xxx','is','xxx','no','xx']
print strings
index = 0
for str in strings:
   if 'xxx' in str:
       strings[index] = 'zzk'
   index += 1
print strings
# ['xxx', 'is', 'xxx', 'no', 'xx']
# ['zzk', 'is', 'zzk', 'no', 'xx']


#跳出循环
#break 跳出
from math import sqrt
for i in range(99,0,-1):   #步长为 -1 使得可以反向迭代
    root = sqrt(i)
    if root == int(root):   #判断是否能整除(能整除的就是 root == int(root)) 不能继续循环
        print i
        break

#continue 让当前循环结束，继续下一次循环----跳过剩余的循环体，继续下一次循环
#不常用，更加应该使用 break

#while True/break 习语,使得一直进行循环
#while True:
#    wor = raw_input('please enter a word:')
#    if not wor:      #这里表示，只要有输入，not wor 就为0 则执行下一句 print ;if 的条件满足时调用break语句 if..break把循环分为两个部分
#        break
#    print 'the word was ' + wor

#while True 实现了一个永远不会退出的循环,

#循环中使用else语句
from math import sqrt
for i in range(99,81,-1):   #步长为 -1 使得可以反向迭代
    root = sqrt(i)
    if root == int(root):   #判断是否能整除(能整除的就是 root == int(root)) 不能继续循环
        print i
        break
else:
    print "Didn't find it!"


