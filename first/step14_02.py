#-*- encoding:utf-8 -*-
#os模块

import os

print os.name
print os.getcwd()
# print os.getenv()
# print os.listdir()
# print os.remove()
# print os.system()
# print os.linesep
print os.path.split('D:\Python\README.txt')
print os.path.isfile('D:\Python\README.txt')
print os.path.exists('D:\Python\README.txt')
source = r'D:\competition\adFeature.csv'
print os.path.exists(source)



