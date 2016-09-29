# coding:UTF-8
__author__ = 'zhongzhikun'
#定义函数
def hello(name):
    return 'Hello, ' + name + '!'

print hello('world')
print hello('zzkaj')
print hello('钟智坤')

print '钟智坤'

#位置参数和关键字参数
def hello1(greeting,name):
    print '%s,%s' %(greeting,name)
hello1('hello','world!')

def hello2(greeting,name):
    print '%s,%s' %(greeting,name)
hello2('world','hello')

hello1(greeting='world',name='hello')
hello1(name='hello',greeting='world')

#关键字参数最好的就是能给函数提供默认参数

#有时候能够让用户自己提供任意的参数是很有用的
def print_params(*params):
    print params
print_params('testing')

print_params(1,2,3)

def print_params2(title,*params):
    print title
    print params
print_params2('params',1,1,2,3)    #可以知道参数前面的星号把所有值都收集起来放在元组里，*的意思就是收集其余参数

#关键字参数的收集工作,收集后面的参数，组成字典输出
def print_params_3(**params):
    print params
print_params_3(x=1,y=2,z=3)

def print_params_4(x,y,z=99,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar
print_params_4(1,2,88,4,5,6,7,foo=1,bar=2)

#实现多个名字的同时存储
def store(data,*full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:names.inser(1,'')
        lables = 'first','middle','last'
        for label,name in zip(labels,names):
            people = lookup(data,lable,name)
            if people:
                people.append(full_name)
            else:
                data[label],[name] = [full_name]

#d={}
#init(d)
#store(d,'han solo')
#store(d,'luke skysky','anakin,skysky')
#lookup(d,'last','skysky')

#参数收集的逆过程
def add(x,y):
    return x + y
params = (1,2)
add(*params)

#练习使用参数

#变量的作用域
def foo():x=42
x = 1
foo()
print x    #foo中的不会影响全局的x

#使用全局变量作为参数名
def output(x):
    print x
x = 1
y = 2
output(y)

#屏蔽引发的问题
#嵌套作用域

#递归，函数自身调用自身
def recursion():
    return recursion() #什么都做不了
#两个经典的递归函数
#计算N的阶乘
def factorial(n):
    result = n
    for i in range(1,n):
        result *=i
    return result
y = factorial(9)
print y
#使用递归的例子
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
yy = fact(9)
print yy

#计算N的幂
def power(x,n):
    result = 1
    for i in range(n):
        result *= x   #这里修改为n的话
    return result
z = power(2,4)
print z
#修改为递归版本，power(x,0)是1，对于大于0的结果，power(x,n)就是x*(x,n-1)的结果
def power1(x,n):    #要有 ：
    if n == 0:   #这里需要是 ==   要有 ：
        return 1
    else:      #要有 ：
        return x * power1(x,n-1)
zz = power1(2,4)
print zz

#理解递归的过程最重要的
#二分法查找











