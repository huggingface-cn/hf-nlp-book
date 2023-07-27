# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
@fix: yaoqi
'''
from __future__ import absolute_import
from format_check import hint, utils,parsing
from format_check.utils import error_solution,strB2Q_some,strQ2B
from format_check.detector.error import errors as errors_describe
import re
__version__ = '1.0.4_fix'

def check(text, ignore='',format='json', fn='anonymous',file_dir=None,format_output=None,auto_fix=False,print_change=True):
    '''check markdown text
    auto_fix: 是否自动修复全部错误
    '''
    ignore_dict = {}
    # 1. 删除代码块
    md_text =re.findall(r'```.*?(.*?)```',  text, flags=re.S)
    text=re.compile(r"```.*?(.*?)```",flags=re.I|re.S).sub('＋－｜－－？ｎ？－－｜－＋',text)
    for code in md_text:
        text=text.replace('＋－｜－－？ｎ？－－｜－＋',f'＋－｜－－？{len(ignore_dict)}？－－｜－＋',1)
        ignore_dict[f'＋－｜－－？{len(ignore_dict)}？－－｜－＋']=f'```{strQ2B(code)}```'
    # 2. 删除图片
    md_text = re.findall(r'(\!\[.*?\]\(.*?\))',  text, flags=re.I|re.S)
    text=re.compile(r"(\!\[.*?\]\(.*?\))",flags=re.I|re.S).sub('＋－｜－－？ｎ？－－｜－＋',text)
    for img_link in md_text:
        text=text.replace('＋－｜－－？ｎ？－－｜－＋',f'＋－｜－－？{len(ignore_dict)}？－－｜－＋',1)
        ignore_dict[f'＋－｜－－？{len(ignore_dict)}？－－｜－＋']=f'{img_link}'
    # 3. 提取链接内容
    md_text = re.findall(r' *(\[((?:[^\\[\]]|\\.)*)\]\(\s*((?:[^\\()\\]|\\.)+)\s*\)) *',  text, flags=re.MULTILINE)
    if auto_fix==False:
        select=input("Markdown链接([]())左右各加一个空格的format？(y/n)")
    else:
        select='y'
    if select=='y':
        print("format Markdown链接([]())")
        md_text=[code[0].strip() for code in md_text]
        md_text=[f' {code} ' for code in md_text]
    text=re.compile(r" *(\[((?:[^\\[\]]|\\.)*)\]\(\s*((?:[^\\()\\]|\\.)+)\s*\)) *").sub('＋－｜－－？ｎ？－－｜－＋',text)
    for link in md_text:
        text=text.replace('＋－｜－－？ｎ？－－｜－＋',f'＋－｜－－？{len(ignore_dict)}？－－｜－＋',1)
        ignore_dict[f'＋－｜－－？{len(ignore_dict)}？－－｜－＋']=f'{link}'
    # 4. 去除 ``
    md_text = re.findall(r' *?(?<!`)`([^`]+?)`(?!`) *?',  text)
    if auto_fix==False:
        select=input("行内代码块（` `)左右各加一个空格的format？(y/n)")
    else:
        select='y'
    if select=='y':
        print("format 行内代码块（` `)")
        md_text=[code.strip() for code in md_text]
        md_text=[f' `{code}` ' for code in md_text]
    text=re.compile(r" *(?<!`)`([^`]+?)`(?!`) *").sub('＋－｜－－ｎ－－｜－＋',text)
    for code in md_text:
        text=text.replace('＋－｜－－ｎ－－｜－＋',f'＋－｜－－{len(ignore_dict)}－－｜－＋',1)
        ignore_dict[f'＋－｜－－{len(ignore_dict)}－－｜－＋']=f'{code}'

    #5.去除Html标签
    md_text = re.findall(r'<.+?>',  text)
    text=re.compile(r"<.+?>").sub('＋－｜－－ｎ－－｜－＋',text)
    for code in md_text:
        text=text.replace('＋－｜－－ｎ－－｜－＋',f'＋－｜－－{len(ignore_dict)}－－｜－＋',1)
        ignore_dict[f'＋－｜－－{len(ignore_dict)}－－｜－＋']=f'{code}'
    md_text = re.findall(r'</?\w+[^>]*>',  text)
    text=re.compile(r"</?\w+[^>]*>").sub('＋－｜－－ｎ－－｜－＋',text)
    for code in md_text:
        text=text.replace('＋－｜－－ｎ－－｜－＋',f'＋－｜－－{len(ignore_dict)}－－｜－＋',1)
        ignore_dict[f'＋－｜－－{len(ignore_dict)}－－｜－＋']=f'{code}'
    md_text = re.findall(r'\[\[.*?\]\]',  text)
    text=re.compile(r"\[\[.*?\]\]").sub('＋－｜－－ｎ－－｜－＋',text)
    for code in md_text:
        text=text.replace('＋－｜－－ｎ－－｜－＋',f'＋－｜－－{len(ignore_dict)}－－｜－＋',1)
        ignore_dict[f'＋－｜－－{len(ignore_dict)}－－｜－＋']=f'{code}'
    text=strB2Q_some(text) 
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
                fix_text=error_solution(errors[0],print_change=print_change)
            else:
                break
            if auto_fix:
                select='y'
            else:
                select=input("是否修复错误？(y/n)")
            if select=='y':
                paragraphs[paragraph]=fix_text
            elif select=='n' and f'{errors[0].code}|{errors[0].index}' not in err_ignore:
                err_ignore.append(f'{errors[0].code}|{errors[0].index}')
    if format_output and file_dir:
        text='\n'.join(paragraphs)
        for ignore_replace in ignore_dict:
            if ignore_replace not in text:
                print(f'Warning:{ignore_replace} not in text content:{ignore_dict[ignore_replace]}')
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


def check_file(fn, ignore='', fmt='text', format_output=True, auto_fix=False,print_change=True):
    ''' Check markdown file
        :param fn: file name
        :param ignore: ignore error code
        :param auto_fix: auto fix error or or comfirm one by one (True/False)
    '''
    with open(fn, encoding='utf-8') as f:
        text = f.read()
        if auto_fix==False:
            print_change=True
        return check(text, ignore, format=fmt, fn=fn, format_output=format_output, file_dir=fn, auto_fix=auto_fix,print_change=print_change)
