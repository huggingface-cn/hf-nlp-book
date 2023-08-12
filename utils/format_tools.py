import format_check
import os

def comfirm(file_name):
    # select=input("Warnding!!! 是否信任格式化后的版本，删除之前的版本?(y/n)")
    # if select=='y':
        os.remove(file_name)
        os.renames('.'.join(file_name.split('.')[:-1]+['_fix']+[file_name.split('.')[-1]]),file_name)
chapter='Course\zh-CN\chapter9'
for i in range(1,len(os.listdir(chapter))):
    file_name=f'{chapter}\\{i}.mdx'
    print(file_name)
    format_check.check_file(file_name,auto_fix=True)
    comfirm(file_name)