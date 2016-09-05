#coding=utf-8
_metaclass_ = type

#魔法方法 属性和迭代器

#构造方法：代表着以前那种名为init的初始化方法，一个对象被创建后，会马上调用构造方法
#python中只要把init方法改成魔法版本，_init_
class FooBar():
    def __init__(self):      #在定义的时候使用魔法版本的_init_
        self.somevar = 42

f = FooBar()
a = f.somevar
print a

###############################################
class FooBar1():
    def __init__(self,value=42):      #在定义的时候使用魔法版本的_init_
        self.somevar = value

f1 = FooBar1('this is a')
a1 = f.somevar
print a1

#重写一般方法和特殊的构造方法
class A:                       #A定义了一个hello的方法，被B类继承
    def hello(self):
        print "hello,I am A"
class B(A):
    pass
a = A()       #创造了一个a的对象
b = B()
a.hello()     #利用 对象.方法 调用A类里面的方法，实现方法的功能
b.hello()

#在子类中增加功能的最基本方式是增加方法，如下面B类重写了超类A中的hello方法
class B(A):
    def hello(self):
        print "hello,I am B"
b = B()
b.hello()

#使用super函数实现子类从超类中继承方法
_metaclass_ = type
class Bird:
    def _init_(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'hhhh...'
            self.hungry = False
        else:
            print 'No,thanks!'
class SongBird(Bird):
    def _init_(self):
        super(SongBird,self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound

#sb = SongBird()
#sb.sing()
#sb.eat()
#sb.eat()








