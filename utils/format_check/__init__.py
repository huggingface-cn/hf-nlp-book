# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
@fix: yaoqi
'''
from __future__ import absolute_import
from hint import hint, utils,parsing
from hint.utils import error_solution
from hint.detector.error import errors as errors_describe
import re
__version__ = '1.0.4_fix'

def check(text, ignore='', format='json', fn='anonymous',file_dir=None,format_output=None):
    '''check markdown text'''
    ignore_dict = {}
    # 1. 删除代码块
    md_text = re.findall(r'```.*?(.*?)```',
                     text, flags=re.I | re.S)
    for code in md_text:
        text=text.replace(f'```{code}```',f'+-|<>?{len(ignore_dict)}?<>|-+')
        ignore_dict[f'+-|<>?{len(ignore_dict)}?<>|-+']=f'```{code}```'
    # 2. 删除图片
    md_text = re.findall(r'(\!\[.*?\]\(.*?\))',  text, flags=re.I|re.S)
    for img_link in md_text:
        text=text.replace(img_link,f'+-|<>?{len(ignore_dict)}?<>|-+')
        ignore_dict[f'+-|<>?{len(ignore_dict)}?<>|-+']=f'{img_link}'
    # 3. 提取链接内容
    md_text = re.findall(r'(\[.*?\]\(.*?\))',  text, flags=re.I|re.S)
    for link in md_text:
        text=text.replace(link,f'+-|<>?{len(ignore_dict)}?<>|-+')
        ignore_dict[f'+-|<>?{len(ignore_dict)}?<>|-+']=f'{link}'
    # 4. 去除 ``
    md_text = re.findall(r'`(.*?)`',  text, flags=re.I|re.S)
    for code in md_text:
        text=text.replace(code,f'+-|<>?{len(ignore_dict)}?<>|-+')
        ignore_dict[f'+-|<>?{len(ignore_dict)}?<>|-+']=f'{code}'

    paragraphs=text.split('\n')
    err_ignore=[]
    for paragraph in range(len(paragraphs)):
        while 1:
            tokens = parsing.tokenizer(paragraphs[paragraph])
            errors = parsing.detect_errors(tokens, paragraphs[paragraph])
            errors=utils.ignore_errorcode(errors, ignore)
            for error in range(len(errors)-1,-1,-1):
                if f'{errors[error].code}|{errors[error].index}' in err_ignore:
                    errors.pop(error)
            if len(errors)>0:
                print(errors[0].format())
                fix_text=error_solution(errors[0])
            else:
                break
            select=input("是否修复错误？(y/n)")
            if select=='y':
                paragraphs[paragraph]=fix_text
            elif select=='n' and f'{errors[0].code}|{errors[0].index}' not in err_ignore:
                err_ignore.append(f'{errors[0].code}|{errors[0].index}')
    if format_output and file_dir:
        text='\n'.join(paragraphs)
        for ignore_replace in ignore_dict:
            text=text.replace(ignore_replace,ignore_dict[ignore_replace])
        with open('.'.join(file_dir.split('.')[:-1]+['_fix']+[file_dir.split('.')[-1]]),'w',encoding='utf-8') as target_f:
            target_f.write(text)
    # check results
    errors = hint.check(text)
    # ignores
    errors = utils.ignore_errorcode(errors, ignore)
            
    # format output array / dict
    errors = {fn: utils.format_errors(errors, format)}
    if format != 'json':
        errors = ['File:%s\n%s' % (k, '\n'.join(es))
                  for k, es in errors.items()
                  if len(es) > 0]
        errors = '\n\n'.join(errors)
    return errors


def check_file(fn, ignore='', format='json',format_output=True):
    '''check markdown file'''
    with open(fn,encoding='utf-8') as f:
        text = f.read()
        return check(text, ignore, format, fn=fn,format_output=format_output,file_dir= fn)
