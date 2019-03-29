# -*- encoding: utf-8 -*-
'''
#面向对象 list  dict
#给另一个对象赋值时，并不是把值传过去，而是这两个对象共享同一个内存

a = [1,2,3]
b = a
b[0] = 0
a[-1] = 4
print b
print a

#创建自己的类与对象
class Mycalss:
    def __init__(self): #构造函数，如果用这个类去实例化一个对象的话，那么这个对象会自动的运行这个构造函数
        print "new object"
        self.name = "mycalss" #self定义，指向对象自己，在python中必须显示出来

a = Mycalss()
print a.name


#给类加入方法
class Mycalss:
    def __init__(self): #构造函数，如果用这个类去实例化一个对象的话，那么这个对象会自动的运行这个构造函数
        print "new object"
        self.name = "mycalss" #self定义，指向对象自己，在python中必须显示出来，所有类中第一个参数必须是self,第二个是传入的名字
    def setname(self,name):
        self.name = name
    def printname(self):
        print self.name

a = Mycalss()
a.setname("Apple")
a.printname()

'''

#继承，代码复用的一个重要方法

class Mycalss:
    def __init__(self): #构造函数，如果用这个类去实例化一个对象的话，那么这个对象会自动的运行这个构造函数
        print "new object"
        self.name = "mycalss" #self定义，指向对象自己，在python中必须显示出来，所有类中第一个参数必须是self,第二个是传入的名字
    def setname(self,name):
        self.name = name
    def printname(self):
        print self.name

class MyNewClass(Mycalss):
    def setage(self,age):
        self.age = age
    def printage(self):
        print self.age

a = MyNewClass()
a.setname("Apple")
a.printname()
a.setage("16")
a.printage()

