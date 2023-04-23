import format_check,os
for file in os.listdir('Course\zh-CN\chapter8'):
    if 'fix'not in file and file=='4.mdx':
        print(file)
        errors = format_check.check_file('Course\zh-CN\chapter8\\'+file, fmt='text',auto_fix=True,print_change=False)
        print(errors)
        print('------------------')