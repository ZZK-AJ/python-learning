#coding=utf-8
print '努力，加油，这是唯一可以给你带来改变的，隐忍，厚积薄发'

#字典：当索引不好用的时候
#序列是通过编号来引用数值的数据结构，字典通过名字来引用值，这种也叫做 映射，字典是python中唯一的内建映射类型
#字典 通过key键找到value值
names = ['zzk','aj','zzkaj']
numbers = ['123','234','1234']       #这里用字符串而不是整数保存了
print numbers[names.index('zzkaj')]
#1234

#这样很麻烦，使用字典解决
phonebook = {'zzk':'123','aj':'234','zzkaj':'12234'}  #这就是一个典型的字典
print phonebook['zzkaj']    #使用 字典名[key] 取出字典的值
#12234

#dict函数 通过这个可以把其他映射的序列建立字典
items = [('name','zzk'),('age','23')]   #把一个元组转换为字典
d = dict(items)
print d
#{'age': '23', 'name': 'zzk'}

c = dict(name='zzk',age=42)
print c
#{'age': 42, 'name': 'zzk'}

#基本的字典操作
# len(d)返回d中项的数量
print len(d)
#2

# d[k]返回关联到键k上的值
print c['name']
# zzk

# d[k]=v 将值v关联到键k上
c['sex'] = 'man'
print c
# {'age': 42, 'name': 'zzk', 'sex': 'man'}

# del d[k]为删除键为k的项
del c['sex']
print c
# {'age': 42, 'name': 'zzk'}

# k in d 检查d中是否有含有键为k的项


#键的类型，可以是任意不可变的 整形，浮点型，字符串或元组
x = {}  #定义一个空的字典
x[42] = 'zzkaj'     #给字典赋值
print x
#{42: 'zzkaj'}



#eg:一个简单的数据库，用人名作为键，每个人名为另一个字典表示 phone和addr表示电话号码和地址
people ={
    'zzk':{
        'phone':'123',
        'addr':'zzk111'
    },
    'aj':{
         'phone':'234',
         'addr':'222'
    },
    'zzkaj':{
          'phone':'1234',
          'addr':'121212'
    }
}
labels = {
    'phone':'phone number',
    'addr':'address'
}

#name = raw_input('Name:')
#request = raw_input('Phone number(p) or address(a)?')

#if request == 'p': key = 'phone'
#if request == 'a': key = 'addr'

#if name in people:
#    print "%s's %s is %s." % (name,labels[key],people[name][key])
#labels[key] 建立lables字典是为了这里显示而已 key 这个参数值得参考 people[name][key] 为调用字典里面的字典的方法


#字典的格式化字符串
print phonebook
#{'zzkaj': '12234', 'aj': '234', 'zzk': '123'}

print "zzk's phone number is %(zzk)s." %phonebook  #这里使用的为 %(zzk)s 就是在%s中间插入了 (zzk)
#zzk's phone number is 123.

#字典的方法
#clear 清除所有字典中项
d = {}
d['name'] = 'zzk'
d['age'] = '23'
print d
# {'age': '23', 'name': 'zzk'}
return_value = d.clear()
print d
print return_value
# {}
# None

#copy 返回一个具有相同 键-值 的新字典，这个方法实现的是浅复制
x = {'usename':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['usename'] = 'zzk'
y['machines'].remove('bar')
print y
print x
#output
#{'machines': ['foo', 'baz'], 'usename': 'zzk'}
#{'machines': ['foo', 'baz'], 'usename': 'admin'}
#可以看到，使用 remove在两者中都删去了 bar 但是修改的话，只修改了 y

from copy import deepcopy
yy = deepcopy(x)
print yy
yy['machines'].append('aj')
print yy
print x
#{'machines': ['foo', 'baz'], 'usename': 'admin'}
#{'machines': ['foo', 'baz', 'aj'], 'usename': 'admin'}
#{'machines': ['foo', 'baz'], 'usename': 'admin'}

#fromkeys 使用给定的键建立新字典，每个键对应值为none
a = {}.fromkeys(['name','age'])
print a
# {'age': None, 'name': None}

#get 更宽松的访问字典项的方法
d = {}
print d.get('name')
# None

#item iteritems 将字典的项以列表的方式返回 ，列表中每一项为键值对的形式
#.....后面的一些要点略














