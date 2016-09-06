#coding=utf-8
print '文件和流'

#打开文件,open函数
#open(name[,mode[,buffering]] 使用一个文件名作为唯一的强制参数，返回一个文件对象
#假如有soefile.txt文件在，存在c:/text
#要打开的话,使用
#f = open(r'c:\text\somefile')

#如果open函数只带一个文件名参数，那么可以获得读取文件内容的文件对象
#如果要想写入内容，必须提供一个模式参数
#指明，读模式和什么模式参数都不用是一样的效果
# + 参数可以用到任何模式中，指明读和写都是允许的
#open 函数中模式参数： 'r'读模式  'w'写模式  'a'追加模式  'b'二进制模式  '+'读写模式

#open函数的第三个参数控制着文件的缓冲，参数为0 I/O输入无缓冲 为1 I/O输入有缓冲(意味着用内存，程序更快)

#基本的文件方法
#类文件对象，支持file类方法的对象，支持read和write方法
# 如urllib和urllib2，支持read，readline和readlines

#假如有名为f的类文件对象，那么就有f.write和f.read方法
f = open('somefiles.txt','r')
print f.read()
#this is somefiles in here
f.close()

f = open('somefiles.txt','w')
f.write('Hello World!')
f.close()
f = open('somefiles.txt','r')
print f.read()
#print f.read(4)

f = open('somefiles.txt','a')
f.write('aj will @ zzk!')
f.close()
f = open('somefiles.txt','r')
print f.read()
print '*******************'

#读写行
#readline方法，读取单独一行。
#readlines方法，读取所有行，并将其作为列表返回
#writelines方法，给一个字符串列表，把所有字符写入文件

#关闭文件，写入的文件最好关闭。
#或者使用with语句，会自动关闭
for i in range(3):
    with open("somefiles.txt",'a') as somefiles:   #相当于原来的 somefiles = open('somefiles.txt','r')
        somefiles.write('zzk @ aj!')

with open("somefiles.txt", 'r') as somefiles:
    print somefiles.read()

print '*******************'
#使用文件的基本方法：
#readline
f = open(r'somefiles.txt')
for i in range(3):
    print str(i) + ':' + f.readline()

import pprint
pprint.pprint(open(r'somefiles.txt').readlines())

print '*******************'

f = open(r'somefiles.txt','w')
f.write('this\n is\n my\n offer\n')
f.close()
f = open(r'somefiles.txt')
with open(r"somefiles.txt") as files:
    print str(i) + ':' + files.readline()

#对文件内容迭代
#按字节处理，用read方法对每个字符进行循环
print '*******************'
def process(string):
    print 'processing:',string

f = open(r'a.txt')
while True:
    char = f.read(1)
    if not char:
#需要的是假如读入的是一个char(只是代指一个变量而已)，那么就使用process函数处理，假如不是一个字符串，那么就继续循环
        break        #if 判断的依据是，假如是char变量 则not char为0 不满足if判断的条件 只有是空字符时，才执行到break
    process(char)
f.close()

print '*******************'
with open(r"a.txt") as f:
    while True:
        char = f.read(2)
        if not char:
            break
        process(char)

#按行处理
print '*******************'
with open(r"a.txt") as f:
    while True:
        line = f.readline()   #读取一行，赋给line变量，假如line变量不为空，则执行process函数
        if not line:
            break
        process(line)

#读取所有内容
#将文件的内容读入一个字符串或者读入列表也很有用，比如在读取后，可以对字符串进行正则表达式操作
#使用read迭代每个字符
print '*******************'
f = open(r'a.txt')
for char in f.read():  #这里就是把char = f.read()的值
    process(char)
f.close()
#从结果可以看出，换行符是不能

#按行迭代
print '*******************'
f = open(r'a.txt')
for line in f.readlines():  #这里就是把char = f.read()的值
    process(line)
f.close()

#但要对一个很大的文件进行迭代操作时，readlines会占用太多内存
#使用while循环和readline代替，如果能够使用for循环，就用for循环
#使用fileinput来对行进行迭代
print '*******************'
import fileinput
for line in fileinput.input(r'a.txt'):
    process(line)

#文件迭代器
print '*******************'
for line in open(r'a.txt'):
    process(line)

print '*******************'
f = open('b.txt','w')
f.write('first line\n')
f.write('second line\n')
f.write('third line\n')
f.close()
#完成写入了三行
lines = list(open('b.txt'))    #用list方法 使得文本转换为字符串列表
print lines
#['first line\n', 'second line\n', 'third line\n']
theone, thetwo, thethree = open('b.txt')
print theone
print thetwo
print thethree



























