# -*- encoding: utf-8 -*-
#文件备份
#每日备份，时间为压缩文件名
import os
import time

source = r'C:\Users\zhongming\Desktop\test'
#source = r'D:\test'

target_dir= r'D:\try\\'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

winrar_command = "WinRAR a %s %s"%(today,source)

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

comment = raw_input('Enter a comment ->')
if len(comment) == 0:
    target = today + os.sep + now +'.rar'  #os.sep 会根据操作系统给出目录分隔符
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ','_') + '.rar'

winrar_command = "WinRAR a %s %s"%(target,source)

if os.system(winrar_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'