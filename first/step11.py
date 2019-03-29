#-*- encoding:utf-8 -*-
#创建一个类

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print 'hello, my name is', self.name

p= Person('steph')
p.sayHi()
