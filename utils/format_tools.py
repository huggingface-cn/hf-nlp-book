import format_check,os
for file in os.listdir('./tests/md'):
    if 'fix'not in file:
        print(file)
        errors = format_check.check_file('./tests/md/'+file, format='text')
        print(errors)
        print('------------------')