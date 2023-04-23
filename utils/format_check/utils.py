# -*- coding: utf-8 -*-
'''
Created on 2016-12-13

@author: hustcc
'''
from __future__ import absolute_import
import os
import copy
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[0;92;42m'
    WARNING = '\033[0;31;43m'
    DANGER = '\033[0;31;41m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def strB2Q(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 32:                                 #半角空格直接转化                  
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
            inside_code += 65248
        rstring += chr(inside_code)
    return rstring
def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288:                              #全角空格直接转换            
            inside_code = 32 
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248

        rstring += chr(inside_code)
    return rstring


def is_latin(c):
    '''decide c is latin or not
    '''
    return c.isalpha()

def is_B_c(c):
    """半角符号判断"""
    inside_code=ord(c)
    return 0x0020<=inside_code<=0x7e

def is_space(c):
    '''decide c is space，中文
    '''
    return c.isspace()


def is_number(c):
    # 是否是数字
    return c in '1234567890'


def is_unit(c):
    # 判断是否为单位
    return 'TODO'


def is_fw_symbol(c):
    # 是否为中文符号
    return c in u'，。；：、？！'


def is_hw_symbol(c):
    # 是否为中文符号
    return c in ',.;:\?!'


def is_ellipsis_symbol(c):
    # 是否是省略号
    return c in u'…'


def is_fw_number(c):
    # 是否是圆角数字
    return c in u'０１２３４５６７８９'


def is_zh(c):
    '''判断是否为中文'''
    return u'\u4e00' <= c <= u'\u9fff' and True or False


def is_zh_unit(c):
    '''判断是否为单位'''
    return c in u'％℃°'


def ignore_errorcode(errors, ignores):
    '''ignore the errors in ignores
    '''
    if not isinstance(ignores, list):
        ignores = ignores.split(',')
    # trim the error code
    ignores = [code.strip() for code in ignores]
    # ignore error codes.
    errors = [error for error in errors if error.code not in ignores]
    return errors


def format_errors(errors, format):
    return [e.format(format) for e in errors]


def typeof(c):
    if is_number(c):
        return 'N'  # number
    if is_zh_unit(c):
        return 'U'  # zh unit
    if is_space(c):
        return 'S'  # space
    if is_ellipsis_symbol(c):  # 省略号
        return 'E'
    if is_fw_symbol(c):
        return 'H'  # zh sym
    if is_hw_symbol(c):
        return 'I'  # en sym
    if is_fw_number(c):
        return 'F'  # 全角 number
    if is_zh(c):
        return 'Z'  # zh
    if is_latin(c):
        return 'L'  # latin
    return 'O'  # other， no limit


detectors_on = None


def load_detectors():
    '''加载所有的检测器'''
    # 缓存一下，避免多次加载
    global detectors_on
    if detectors_on:
        return detectors_on

    from hint.detector import exxx
    detectors_on = [exxx.Detector]

    return detectors_on


# 使用非递归的方式，来遍历目中的所有 markdown 文件
def traversing_path_norecursive(all_files, path,
                                depth=0,
                                max_depth=3,
                                suffixs=['.md']):
    paths = [path]  # 需要被循环遍历的目录数组
    # 遍历深度限制
    paths_tmp = []  # 临时存储每次遍历的目录
    pj = os.path.join
    while depth <= max_depth:
        # 目录，新增一级
        depth += 1
        # 遍历这些目录
        for path in paths:
            ls = os.listdir(path)  # 目录中所有的文件，文件夹
            # 所有文件
            files = [f for f in ls if os.path.isfile(pj(path, f))]
            # 符合后缀名称的文件，添加到最后的 all_files 中
            all_files += [
                pj(path, f) for f in files if f[-3:] in suffixs
            ]

            # 所有文件夹，加入到待遍历数组中
            paths_tmp += [
                pj(path, d) for d in ls if os.path.isdir(pj(path, d))
            ]
        paths = copy.deepcopy(paths_tmp)
        # 每次遍历一层之后初始化
        paths_tmp = []

    return all_files
def error_solution(error,print_change=True):
    if error.code=='E101' or error.code=='E102':
        if error.text[error.index].isalpha() or error.text[error.index].isdigit():
            fix_text=error.text[:error.index]+' '+error.text[error.index:]
            if print_change:
                print(f"{error.text[:error.index]}{bcolors.OKGREEN} {bcolors.ENDC}{error.text[error.index:]}")
        else:
            fix_text=error.text[:error.index+1]+' '+error.text[error.index+1:]
            if print_change:
                print(f"{error.text[:error.index+1]}{bcolors.OKGREEN} {bcolors.ENDC}{error.text[error.index+1:]}")
        return fix_text
    elif error.code=='E103':
        fix_text=error.text[:error.index]+error.text[error.index+1:]
        if print_change:
            print(f"{error.text[:error.index]}{bcolors.DANGER} {bcolors.ENDC}{error.text[error.index+1:]}")
        return fix_text
    elif error.code=='E104':
        if error.text[error.index+1] in '％℃°nx':
            fix_text=error.text[:error.index]+error.text[error.index+1:]
            if print_change:
                print(f"{error.text[:error.index]}{bcolors.DANGER} {bcolors.ENDC}{error.text[error.index+1:]}")
        else:
            fix_text=error.text[:error.index]+' '+error.text[error.index:]
            if print_change:
                print(f"{error.text[:error.index]}{bcolors.OKGREEN} {bcolors.ENDC}{error.text[error.index:]}")
        return fix_text
    elif error.code=='E201':
        fix_text=error.text[:error.index]+error.text[error.index+1:]
        if print_change:
            print(f"{error.text[:error.index]}{bcolors.DANGER}{error.text[error.index]}{bcolors.ENDC}{error.text[error.index+1:]}")
        return fix_text
    elif error.code=='E201':
        fix_text=error.text[:error.index]+error.text[error.index+1:]
        if print_change:
            print(f"{error.text[:error.index]}{bcolors.DANGER}{error.text[error.index]}{bcolors.ENDC}{error.text[error.index+1:]}")
        return fix_text
    elif error.code=='E202':
        if is_B_c(error.text[error.index]):   
            fix_text=error.text[:error.index]+strB2Q(error.text[error.index])+error.text[error.index+1:]
            if print_change:
                print(f"{error.text[:error.index]}{bcolors.WARNING}{strB2Q(error.text[error.index])}{bcolors.ENDC}{error.text[error.index+1:]}")
        elif is_B_c(error.text[error.index-1]):   
            fix_text=error.text[:error.index-1]+strB2Q(error.text[error.index-1])+error.text[error.index:]
            if print_change:
                print(f"{error.text[:error.index-1]}{bcolors.WARNING}{strB2Q(error.text[error.index-1])}{bcolors.ENDC}{error.text[error.index:]}")
        return fix_text
    elif error.code=='E203':
        fix_text=error.text[:error.index-1]+strQ2B(error.text[error.index-1])+error.text[error.index:]
        if print_change:
            print(f"{error.text[:error.index-1]}{bcolors.WARNING}{strQ2B(error.text[error.index-1])}{bcolors.ENDC}{error.text[error.index:]}")
        return fix_text
    elif error.code=='E204':
        if(error.index<len(error.text)-1 and error.text[error.index-1]=='…' and error.text[error.index]!='…' and error.text[error.index-2]!='…') or \
        (error.index-2<0 and error.text[error.index-1]=='…' and error.text[error.index]!='…') or \
        (error.index==len(error.text)-1 and error.text[error.index-1]=='…' and error.text[error.index-2]!='…'):
            fix_text=error.text[:error.index-1]+'……'+error.text[error.index:]
            if print_change:
                print(f"{error.text[:error.index-1]}{bcolors.WARNING}……{bcolors.ENDC}{error.text[error.index:]}")
        else:
            start=error.index
            end=error.index
            while(start>0 and error.text[start-1]=='…'):
                start-=1
            while(end<len(error.text)-1 and error.text[end+1]=='…'):
                end+=1
            fix_text=error.text[:start]+'……'+error.text[end+1:]
            if print_change:
                print(f"{error.text[:start]}{bcolors.WARNING}……{bcolors.ENDC}{error.text[end+1:]}")
        return fix_text
    elif error.code=='E205':
        fix_text=error.text[:error.index-1]+error.text[error.index:]
        if print_change:
            print(f"{error.text[:error.index-1]}{bcolors.DANGER} {bcolors.ENDC}{error.text[error.index:]}")
        return fix_text
    elif error.code=='E301':
        fix_text=error.text[:error.index-1]+strQ2B(error.text[error.index-1])+error.text[error.index:]
        if print_change:
            print(f"{error.text[:error.index-1]}{bcolors.WARNING}{strQ2B(error.text[error.index-1])}{bcolors.ENDC}{error.text[error.index:]}")
        return fix_text
if __name__ == '__main__':
    print(traversing_path_norecursive([], 'E:/Work/git_code/hint',
                                      max_depth=4))
