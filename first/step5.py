# -*- encoding:utf-8 -*-

#列表推导和字典推导
'''
numbers = [1,2,3,4,5,6]

#偶数抽出来，组成新的数组
#传统方法1
even = []
for i in numbers:
    if i%2 ==0:
        even.append(i)
print even
#列表推导2
even = [i for i in numbers if i%2 == 0]
print even

#如果要得到一个数组，这个数组是数组中每个元素都乘以2
test = [i*2 for i in numbers]
print "test",test


#判断一个变量值是否落在一个范围之内
if a >1 and a<10 #其他编程语言

if 1 < a < 10 #python


#迭代数组，并输出每个元素，遇到负数则终止循环
#增加新需求，判断这个数组里的元素是不是都是正数
num = [1,2,3,-4,5]
for i in num:
    if i<0:
        break
    print i
else: #执行完整个for没有退出，则会执行else
    print "all nums are positive"
'''

#集合操作
A = {1,2,3,4}
B = {4,5,6}
print A|B
print A&B

def someFunction():
    pass

print someFunction()


