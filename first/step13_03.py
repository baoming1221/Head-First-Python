#-*- encoding:utf-8 -*-
#使用 try finally

import time

try:
    f = file('test.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line
finally:
    f.close()
    print 'Cleaning up...closed the file'