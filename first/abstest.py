# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 16:02
# @Author  : Alessia
# @Email   : baoming1221@126.com
# @File    : abstest.py
# @Software: PyCharm

def abs_mat(a):
    if not isinstance(a,(int,float)):
        raise TypeError('bad operand type')
    if a > 0:
        return a
    else:
        return -a



