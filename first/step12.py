#-*- encoding: utf-8 -*-
#使用文件
test = '''
just test for the future!
'''

f = file('aa.txt','w') #open for 'w'riting
f.write(test) #write text to file
f.close()

f = file('aa.txt')
#if no mode is sepcified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0: # zero length indicates EOF
        break
    print line
    #Notice comma to avoid automatic newline added by python
f.close()

