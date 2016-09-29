#coding=utf-8
print "%s is number %d!" % ("Python" ,1)

#user = raw_input('input your login name:')
#print 'your login name is :',user      #,号很重要

#num = raw_input('enter number:')
#print 'doubling you number: %d' % (int(num) *2)


#字符串赋值和使用索引操作符[],切片操作符[:],使用+拼接字符串，使用*字符串重复
pystr = 'python'
zzk = 'better'
print pystr[0]
#p
print pystr[1]
#y
print pystr[-1]
#n
print pystr[1:3]
#yt
print pystr + zzk
#pythonbetter
print zzk * 2
#betterbetter

#列表
alist = [1,2,3,4]  #定义一个列表
print alist
#[1, 2, 3, 4]
print alist[0]  #和字符串操作一样
#1
print alist[1]
#2
print alist[-1]
#4
print alist[0:2]    #列表的切片
#[1, 2]
print alist[:2]
#[1, 2]
alist[0]= 'zzk' #列表的赋值
print alist
#['zzk', 2, 3, 4]

#元组
atuple = ('zzk',zzk,30)
print atuple
#('zzk', 'better', 30)
print atuple[:3]
#('zzk', 'better', 30)

#atuple[1] = 'better'    这个是不允许的，元组只能读

#字典
adict = {'host':'192.168.10.1'} #定义一个字典
print adict
#{'host': '192.168.10.1'}
adict['port'] = 80  #往字典里添加一个新的项，指定key和value
print adict
#{'host': '192.168.10.1', 'port': 80}
print adict.keys()  #使用keys方法返回所有键，返回的是一个列表的形式
#['host', 'port']
print adict.values()    #使用values方法返回所有值
#['192.168.10.1', 80]
print adict['host']     #使用adict['host']取出host对应的value
#192.168.10.1
for a in adict:       #轮询字典,a进入字典后，得到的是key，而adict[a]就是value了
    print a,adict[a]
#host 192.168.10.1
#port 80





