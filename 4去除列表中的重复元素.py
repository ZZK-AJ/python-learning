#coding=utf-8

l1 = ['b','c','d','b','c','a','a']

#使用集合,集合里面没有重复的？
aa = set(l1)
print aa
#set(['a', 'c', 'b', 'd'])
a = list(set(l1))
print a

#用字典
b = {}.fromkeys(l1).keys()
print b

#用字典并保持顺序
c = list(set(l1))
c.sort(key=l1.index)
print c

#列表推导式
d = []
[d.append(i) for i in l1 if not i in d]
print d

#还可以先排序，后删除?????

print l1.sort


