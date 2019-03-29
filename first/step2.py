# -*- coding: UTF-8 -*-
'''
print "hello"
print "world"

print "hello","world"

# 输入值
a = raw_input();
print "my number is", a

print "helo\"world"


print len("heieywnw")

print str(123)+"123"
print int(123)+123


print "hello"[0]

print "hello"[-1]

print "abcdefg"[1:3]
print "abcdefg"[:3]
print "abcdefg"[3:]
print "abcdefg"[:]

print "abcdefg"[::2]
print "abcdefg"[::-2]


a = [1,2,3,4,5]
a.append(6)
a.append(7)
print a

a = [1,2,0.03,"hello",[1,2,3]]
print a[0]
print a[-1]
print a[-1][0]


a=[1,2,3]
b=[4,5,6]
print a+b

print a*3

a = [1,2,3,4,5]
del a[0]
print a

a = [1,2,3,4,5]
a.insert(2,2.5)
print a

a.append(6)
a.append(7)
print a
'''
#字典
contact = {"lilei":"0101234","hanmeimei":"0102345"}
contact["lucy"] = "0102567"
#contact["lilei"] = "02012345"
del contact["lilei"]
print contact
print contact["hanmeimei"]


