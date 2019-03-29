# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 15:21
# @Author  : Alessia
# @Email   : baoming1221@126.com
# @File    : lxf_01.py
# @Software: PyCharm

#print absolute value of an integer:

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

print('''a adff
...badfsadf
...asdfasdf''')

print(r'''adfadf,\n
baby''')

# -*- coding: utf-8 -*-
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n,f,s1,s2,s3,s4)

from abstest import abs_mat
print(abs_mat(-1))

import math

def move(x,y,step,angle):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    return nx,ny

print(move(10,20,4,30))

def person(uername,age,**kw):
    print("name:",uername,'age:',age,"other:",kw)

person("ABB",18)
person("ddd",6,city="SH")
extra = {"city":"HK","job":"engineer"}
person("yyy",5,**extra)

#关键字参数
def person1(name,age,**kw):
    if 'city' in kw:
        pass
    if "job" in kw:
        pass
    print("name:",name,'age:',age,"other:",kw)

person1("dddfd",6,city="SH",adf="124")

#命名关键字参数
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name,age,*,city,job):
    if 'city' in city:
        pass
    if "job" in job:
        pass
    print("name:",name,'age:',age,"city:",city,'job:',job)

person2("dddfd",6,city="SH",job="124")

#命名关键字参数必须传入参数名，这和位置参数不同
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符
#如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
def person2(name,age,*,city="HK",job):
    if 'city' in city:
        pass
    if "job" in job:
        pass
    print("name:",name,'age:',age,"city:",city,'job:',job)

person2("dddfd",6,job="cleaner")
