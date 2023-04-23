import os
import yaml
import re
import pandas as pd
sumery_dict={"title":[],"words_num":[]}
dict_file=yaml.load(open('translate_course\course\chapters\en\_toctree.yml','r',encoding='utf-8'))
for chapter in dict_file:
    title=chapter['title']
    words=0
    for file in chapter['sections']:
        words=len(re.sub("'''.*?'''", "", open('translate_course\course\chapters\zh-CN\\'+file['local']+'.mdx','r',encoding='utf-8').read(),flags=re.MULTILINE|re.DOTALL))
        sumery_dict['title'].append(file['local']+"  "+file['title'])
        sumery_dict['words_num'].append(words)
    # print(f'{title}|{words}')
data=pd.DataFrame(sumery_dict)
data.to_markdown('translate_course\summery.md',index=False)
data.to_csv('translate_course\summery.csv',index=False)
