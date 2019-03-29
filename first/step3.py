# -*- coding: utf-8 -*-

'''
print 1+1 == 2
print 1+1 == 3
print 1+1 != 3
print 1+1 != 2


#与 and
print 1+1 ==2 and 1+1 !=3
print 1+1 !=2 and 1+1 !=3

#或 or
print 1+1 ==2 or 1+1 !=3

#取反 not
print not 1+1 != 2

#判断list中有个元素是否存在 in
a = [1,2,3,4]
print 1 in a
print 6 in a


#if控制程序执行
light = "red"
if light == "red":
    print "Stop"
else:
    print "Go"

light = "yellow"
if light == "red":
    print "Stop"
elif light == "green":
    print "Go"
elif light == "yellow":
    print "Slow down"

#while for 执行重复
while exp:
    print a
    print b
print c

sum = 0
i = 1
while i <=100:
    sum += i
    i += 1
print sum

#for循环可以自动遍历list 或 dict
num = [0,1,2,3,4]
for i in num:
    print i


contact = {"lilei":"0101234","hanmeimei":"0102345"}
for i in contact:
    print i,contact[i]

#遇到负数停止输出
num = [0,1,2,3,-4,5]
for i in num:
    if i < 0:
        break
    print i

#遇到负数不输出
num = [0,1,2,3,-4,5]
for i in num:
    if i < 0:
        continue
    print i

#操作打包- 函数

num = [0,1,2,3,4,5]

def addsum(num):
    sum = 0
    for i in num:
        sum += i;
    return sum  #程序执行后返回一个值

num2  = [2,5,7,9]

print addsum(num)
print addsum(num2)


#作用域
x = 1

def changex():
    global x  #声明全局x，进行修改
    x = 10
    print "x in function", x

changex()
print x  #函数内的X和函数外的X是两个不同的X，在两个不同的作用域是互相看不见的
'''

#函数重打包 - 模块

import math

print math.pi
print math.sin(math.pi/2)

print dir(math) #通过dir函数可查看这个包提供哪些功能

