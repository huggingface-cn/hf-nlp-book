import pandas as pd
from markdown_it import MarkdownIt
import numpy as np  
import re
#从glossary.md中提取glossary
#把翻译中出现的英文术语和常用缩写给出提示
#限制,glossary.md中的表格必须是6列,并且包含英文术语,中文翻译,常用缩写三列
def extract_tables_from_tokens(tokens):
    tables = []
    current_table = []
    in_table = False
    for token in tokens:
        if token.type == "table_open":
            in_table = True
        elif token.type == "table_close":
            in_table = False
            tables.append(current_table)
            current_table = []
        elif in_table and token.type == "inline":
            row = []
            for child in token.children:
                if child.type == "text":
                    row.append(child.content)
            current_table.append(row)
    return tables

def trans_to_dict():
    markdown_file = 'glossary.md'
    markdown_text = open(markdown_file, 'r', encoding='utf-8').read()
    md = MarkdownIt("commonmark").enable("table")
    tokens = md.parse(markdown_text)
    tables=[]
    #从tokens中提取表格token
    for table_token in extract_tables_from_tokens(tokens):
        table=[]
        for token in table_token:
            if token:
                table.append(token[0])
            else:
                table.append('')
        tables.append(table)
    #将表格token转换为dataframe
    data_frames = [pd.DataFrame(np.array(table[6:]).reshape(-1,6), columns=[i for i in table[:6]]) for table in tables]
    data_frames=[data_frame[['英文术语', '中文翻译','常用缩写']].dropna() for data_frame in data_frames]
    #将dataframe转换为字典
    dict=[data_frame.set_index('英文术语')['中文翻译'].to_dict() for data_frame in data_frames]+[data_frame.set_index('常用缩写')['中文翻译'].to_dict() for data_frame in data_frames]
    res={}
    for d in dict:
        res.update(d)
    res.pop('')
    return res
find_all = lambda c, s: [x for x in range(c.find(s), len(c)) if c[x] == s]
def main(file_name):
    doc=open(file_name, 'r', encoding='utf-8')
    trans_dict=trans_to_dict()
    line_count=1
    for line in doc.readlines():
        for string in trans_dict:
            if string in line:
                #查找列号
                col=[m.start() for m in re.finditer(string, line)]
                print(f'line {line_count}, Col {col}: {string}:{trans_dict[string]} ')
        line_count += 1
if __name__ == '__main__':
    main(r'Course\en\chapter8\1.mdx')

