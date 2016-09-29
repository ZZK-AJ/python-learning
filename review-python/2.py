#coding=utf-8
#if语句
i = 3
if i<0:
    zzk = 'zzk will do better'
    print zzk
    zzk1 = {'a':'zzk will','b':'better'}
    print zzk1
    be = 'be'
    zzk2 = ['zzk','will',be,'better']
    print zzk2
    zzk3 = ('zzk','will,be')
else:
    print 'zzk is better than better'

#zzk will do better

#{'a': 'zzk will', 'b': 'better'}

#['zzk', 'will', 'be', 'better']

#while语句
a = 1
while a > 1:
    print 'zzk'

#for循环和range()内建函数
for i in ['zzk','zzk1','better']:
    print i
#zzk
#zzk1
#better

for a in range(3):   #迭代次数
    print a
#0
#1
#2


foo = 'abc'     #迭代字符串
for a in foo:
    print a
#a
#b
#c

for i in range(len(foo)):  #显示各一个元素和索引值
    print foo[i],'(%d)' %i
#a  (0)
#b  (1)
#c  (2)

#列表解析
ss = [x ** 2 for x in range(4)]
for i in ss:
    print i
#0
#1
#4
#9

#文件和内建函数open(),file()
filename = raw_input('Enter file name: ')      #输入一个文件名，然后打开这个文件1.txt，f是先把文件全部读到了f里面
f = open(filename,'r')                      #全部读到f里面以后，再进行每行迭代输出
for eachline in f:
    print eachline
f.close()

#错误和异常
try：
    filename = raw_input('Enter file name: ')  # 输入一个文件名，然后打开这个文件1.txt，f是先把文件全部读到了f里面
    f = open(filename, 'r')  # 全部读到f里面以后，再进行每行迭代输出
    for eachline in f:
        print eachline
    f.close()
except: IOError,e:
    print 'file open error',e






