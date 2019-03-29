# -*- encoding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#文件备份
import os
import time

source = r'C:\Users\zhongming\Desktop\test'
#source = r'D:\test'

target_dir= r'D:\try\\'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'

winrar_command = "WinRAR a %s %s"%(target,source)

if os.system(winrar_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'