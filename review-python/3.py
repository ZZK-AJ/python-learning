#coding=utf-8
#函数
def zzk():
    z = 'zzk brtter'
    print z
    for i in range(len(z)):
        print i,z[i]
    zz = ['a','b','c']
    for i in range(len(zz)):
        print i,zz[i]
zzk()
#zzk brtter
#0 z
#1 z
#2 k
#3
#4 b
#5 r
#6 t
#7 t
#8 e
#9 r

#0 a
#1 b
#2 c

#调用参数，返回值
def add(x):
    return x+x
print add(5)
#10

#默认参数
def foo(debug=True):
    if debug:
        print 'in debug mode'
    print 'done'

print foo()


#类


#模块
import sys
print sys.stdout.write('hello world!')
print sys.platform
print sys.version
#hello world!
#win32
#2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:40:30) [MSC v.1500 64 bit (AMD64)]

#实用的函数
# int([obj])   #把一个对象转为整形
# len([object]) #返回对象的长度
# open(filename,mode)   #打开文件，mode为'r'读 'w'写
# range([[start][stop]])    #返回一个整形列表
# raw_input(str)    #等待输入一个字符串，str为提示作用
# str()     #将一个对象转换为字符串


for i in range(10):
    if i<5:
        continue #不往下走了,直接进入下一次loop
    print("loop:", i )
# ('loop:', 5)
# ('loop:', 6)
# ('loop:', 7)
# ('loop:', 8)
# ('loop:', 9)

for i in range(10):
    if i>5:
        break #不往下走了,直接跳出整个loop
    print("loop:", i )

# ('loop:', 0)
# ('loop:', 1)
# ('loop:', 2)
# ('loop:', 3)
# ('loop:', 4)
# ('loop:', 5)









