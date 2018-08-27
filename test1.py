#-----------一   analysis 分析         --------------------#

#1.目的：为了实现数据安全和可追溯历史



#-----------二   design 设计           --------------------#

#2.功能/方法：使用zip压缩打包软件对指定目录进行定期备份





#-----------三   inplementation 实现   --------------------#

#3.步骤/流程：
#A.指定需要备份文件目录
#B.指定文件需要备份到哪个目录
#C.指定备份后文件命名方法，便于追溯和还原
#D.配置备份参数，进行备份




#-----------4   testing 测试          --------------------#


#-----------5   deployment 部署        -------------------#


#-----------6   mantence 维护         --------------------#


#-----------7   bug fixing 修复       --------------------#










#----------------------------------------------------------------#
#-------------------------code     start-------------------------#
#----------------------------------------------------------------#


import time
import os


DRIVE = 'E:'
PATH = DRIVE + os.sep + 'py'
SOURCE = [PATH]
target_dir = DRIVE + os.sep+'backup'+ '_' + 'pythonfile'
target = time.strftime('%Y%m%d') + time.strftime('%H%M%S')

zip_command = 'zip -r {0} {1}'.format(target_dir+os.sep+target+'.zip',' '.join(SOURCE))

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Create target dir successfully')


print('DRIVE:',DRIVE)
print('PATH:',PATH)
print('SOURCE:',SOURCE)
print('target_dir:', target_dir)
print('target:', target)
print('zip command is :',zip_command)
print('Running:')

if os.system(zip_command)==0:
    print('Successfully backup to ',target_dir)

else:
    print('Backup to {0} FAILED',target_dir)




#----------------------------------------------------------------#
#-------------------------code       end-------------------------#
#----------------------------------------------------------------#





