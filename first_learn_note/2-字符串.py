#coding=utf-8

#基本字符串操作：

#字符串格式化
format = "hello,%s. %s enough for you?" #这里的两个%s就是要求格式化的位置，%s为字符串，%d为数字
values = ('world','hot')  #这里是一个元组
print format %values    #format 这个字符串，里面有格式化的位置，使用values的值进行格式化

# % 左侧放一个字符串，右侧放一个希望被格式化的值，可以是一个字符串或者数字，也可以多个值的元组或者字典
# %s 为转换说明符 标记了需要插入的转换值的位置，s表示值会被格式化为字符串
# hello,world. hot enough for you?


#字符串格式化，完整版
print '%s plus %s equals %s' % (1,1,2)
# 1 plus 1 equals 2

#详细内容看书本的内容

#字符串的方法
#find方法 在一个较长的字符串中查找子串 返回子串所在位置最左端索引
print 'with a moo-moo here,and here moo'.find('moo')
#7

title = 'monty python flying sky'
print title.find('python')
#6

#join 是split的逆方法，用字符串来连接序列的元素 被连接的序列元素必须是字符串
seq = ['1','2','3','4','5']   #列表
a = '+++++++'
b = '+'
print a.join(seq)
#1+++++++2+++++++3+++++++4+++++++5
print b.join(seq)
#1+2+3+4+5

dirs = ['','usr','bin','env']
print '/'.join(dirs)
#/usr/bin/env
print 'C:' + '\\'.join(dirs)
#C:\usr\bin\env

#lower 返回字符串的小写字母版本
print 'ttttTTTTTTTTTtttt'.lower()
#ttttttttttttttttt

name = 'ZZK'
names = 'zzk aj '
if name in names:
    print 'found it！！！！！！！！！！!'
if name.lower() in names:
    print 'found it!'
# found it


#replace 方法 返回某字符串所有匹配项都被替换后得到的字符串
print 'this a place to a repalce '.replace('a','zzk')   #实现查找替换功能
#this zzk plzzkce to zzk repzzklce

#split,join的逆方法，用来将字符串分割成序列
print '1+2+3+4+5'.split('+')
#['1', '2', '3', '4', '5']

print '/usr/bin/env'.split('/')
#['', 'usr', 'bin', 'env']

print 'using the default'.split()
#['using', 'the', 'default']



