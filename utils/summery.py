import os
import yaml
import re
import pandas as pd
sumery_dict={"title":[],"words_num":[]}
# 读取zh-CN目录
dict_file=yaml.load(open('Course\en\_toctree.yml','r',encoding='utf-8'))
for chapter in dict_file:
    title=chapter['title']
    words=0
    for file in chapter['sections']:
        #去除代码块后统计字数
        # words=len(re.sub("'''.*?'''", "", open('Course\zh-CN\\'+file['local']+'.mdx','r',encoding='utf-8').read(),flags=re.MULTILINE|re.DOTALL))
        words=len(open('Course\zh-CN\\'+file['local']+'.mdx','r',encoding='utf-8').read())
        sumery_dict['title'].append(file['local']+"  "+file['title'])
        sumery_dict['words_num'].append(words)
data=pd.DataFrame(sumery_dict)
data.to_csv('summery.csv',index=False)
