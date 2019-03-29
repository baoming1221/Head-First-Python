#-*- encoding:utf-8 -*-
#列表综合

# a = [2,3,4]
# b = [2*i for i in a if i>2]
# print a,b

#在函数中接受元组和列表

# def powersum(power,*args):
#     '''Return the sum of each argument raised to specified power.'''
#     total = 0
#     for i in args:
#         total += pow(i,power)
#     return total
#
# print powersum(2,3,4)

#lambda形式 用来创建新的函数对象
# def make_repeater(n):
#     return lambda s:s*n
#
# twice = make_repeater(2)
# print twice('word')
# print twice(5)

#exec用来执行储存在字符串或文件中的python语句
# exec 'print "hello"'

#eval用来计算存储在字符串中的有效python表达式
# print eval('2*3')

#assert 用来声明某个条件是真的
# mylist = ['item']
# assert len(mylist) >= 1
# print mylist.pop()
#
# assert len(mylist) >= 1

#repr函数 用来取得对象的规范字符串表示
i = []
i.append('item')
print i
print repr(i)












