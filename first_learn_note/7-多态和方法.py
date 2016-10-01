# coding=utf-8
print 'zzkAI钟智坤andAJ，所以加油每一天'

# 复习相关内容，内建对象类型(数字，字符串，列表，元组和字典)
# 内建函数和标准库的用法，定义函数的方法处，接下来要创建自己的对象


# 更加抽像---自定义对象
# 对象可以看作是数据(特性)，以及一系列可以存取，操作这类数据的方法的组成的集合
# 使用对象代替全局变量和函数
# 使用对象的好处
#   多态：可以对不同类的对象使用同样的操作
#   封装：对外部隐藏对象工作的细节
#   继承：以通用的类为基础创建专门的类对象

# 多态，意味着不知道变量所引用的对象类型是什么，还可以对它进行操作，它也会根据对象的类型不同有不同的行为
# 多态和方法：
# 程序接收到一个对象，不了解内部的实现方式。但是你只要做的是询问价格就够了
# object.getprice()   返回 价格
#   绑定到对象特性上的函数称为方法(method)

a = 'bbaaaabc'.count('a')
print a
aa = ['a', 'a', 1, 1, 1, 2].count(1)
print aa
#4
#3

# 变量x可能包含字符串或是列表，但是x不用关心什么类型，只需要x有一个count的方法，带有一个字符作为参数，返回整数值就够了
from random import choice

x = choice(['hello world', [1, 2, 'e', 'e']])  # 列表[1,2,'e','e']
print x
# [1, 2, 'e', 'e']
b = x.count('e')
print b
#2

# 当不知道对象是什么类型，但又想对对象做点什么的时候，用到多态
# 不限于方法，很多内建运算符和函数都有多态的性质

# 如果需要打印对象长度的函数，只要对象具有长度就可，len函数能用
# repr()函数可以对任何使用
def len_mess(x):
    print "the length of", repr(x), "is", len(x)
c = len_mess('food')
cc = len_mess([1, 2, 3])
# the length of 'food' is 4
# the length of [1, 2, 3] is 3


# 封装，指向程序中的其他部分隐藏具体实现细节的原则
# 多态是让用户不知道是什么类(对象类型)的对象进行方法的调用
# 封装是可以不用关心对象是怎么样构建的而直接使用

# 假如有一个openobject的类
# o = openobject()
#   通过像函数调用那样调用类，将变量o绑定到该对象上，创建了一个对象o
# o.setname('zzk')     使用setname和getname方法对对象操作，假设由openobject类提供
# o.getname() 结果为 zzk

#将数据封装在对象内，将其作为特性存储
#特性作为变量构成对象的一部分，用特性重写类

#继承的概念：可以从让B类从A类里面调用A类的方法，继承了方法

#类---一种对象，所有的对象都属于某一类，称为类的实例
#子类和超类的概念，鸟类和百灵鸟类
#面向对象程序设计过程中，子类的关系是隐式的，一个类的定义取决于她支持的方法
# 类的所有实例(对象)都包含这些方法，所以所有的子类的实例都会包含这些方法

#创建自己的类
_metclass_=type #确定使用新类式，新类式中，需要在模块或者脚本前加上这个赋值语句
class Person:          #Person 为类的名称
    def setname(self,name):     #定义了这三种方法
        self.name = name
    def getname(self):
        return self.name
    def greet(self):
        print "Hello,world!i am %s." % self.name

foo = Person()   #创建了一个foo的对象
bar = Person()

foo.setname('zzk skywalker')
#self使得foo调用方法时，把自己作为第一个参数传入函数中，没有self，成员就无法访问她们要对对象进行操作的本身了
bar.setname('zzkaj skywalker')

foo.greet()
bar.greet()
# Hello,world!i am zzk skywalker.
# Hello,world!i am zzkaj skywalker.

foo.name = 'sure'
foo.greet()
# Hello,world!i am sure.
#知道foo是Person的实例的话，可以把foo.greet()看作Person.greet()简写

print '-------------------------'
class Bird():
    song = 'aaaaaa'
    def sing(self):   #定义了sing这个方法
        # print 'zzzzzzz'
        print self.song

bird = Bird()       #创建了Bird这个类的对象
bird.sing()           #用法是 实例/对象.方法

birdsong = bird.sing  # 变量=实例.方法
birdsong()
# aaaaaa
# aaaaaa

#类的命名空间
class MemberCounter:
    members = 0
    def init(self):
        MemberCounter.members += 1
m1 = MemberCounter()
m1.init()
A = MemberCounter.members
print A
m2 = MemberCounter()
m2.init()
B = MemberCounter.members
print B
#C = m1.members
print m1.members
print m2.members    #类作用域内的变量也可以被所有实例访问


#面向对象设计的思考

#总结：
#   对象：包含特性和方法，特性只作为对象一部分的变量，方法则是存储在对象内的函数
#   (绑定)方法 和 其他函数的区别 在于方法 将对象 作为自己的第一个参数，一般是self
#   类代表对象的集合，每个对象(实例)都有一个类，类的任务是定义它的实例会用到的方法
#   多态，将不同的类和类的对象 进行同样对待的特性，不需要知道对象属于哪个类就能够调用方法




