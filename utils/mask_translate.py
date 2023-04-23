#去除mdx中无法预览的标签
import re
import json
import hashlib
import os
mdx_name='translate_course/course/chapters/zh-CN/chapter8/4.mdx'
def translate_label(mdx_name):
    single_label_type=['FrameworkSwitchCourse','DocNotebookDropdown','Youtube']
    mutiply_label_type=['Tip']
    label_mask_list=[]
    with open(mdx_name,'r',encoding='utf-8') as f:
        mdx=f.read()
    for label in single_label_type:
        label_mask_list+=re.findall(f'< *{label}.*?/>',mdx,re.S)
    for label in mutiply_label_type:
        label_mask_list+=re.findall(f'< *{label}.*?>',mdx,re.S)
        label_mask_list+=re.findall(f'</ *{label}>.*?',mdx,re.S)
    replace_dict={}
    for idx,label in enumerate(label_mask_list):
        replace_dict[f'||++==--{idx}++==--||']=label
        mdx=mdx.replace(label,f'||++==--{idx}++==--||')
    with open(mdx_name.replace('.mdx','_edit.mdx'),'w',encoding='utf-8') as f:
        f.write(mdx)
    json.dump(replace_dict,open(hashlib.md5(mdx_name.encode(encoding='utf-8')).hexdigest()+'.json','w',encoding='utf-8'))
def recover(mdx_name):
    with open(mdx_name.replace('.mdx','_edit.mdx'),'r',encoding='utf-8') as f:
        mdx=f.read()
    replace_dict=json.load(open(hashlib.md5(mdx_name.encode(encoding='utf-8')).hexdigest()+'.json','r',encoding='utf-8'))
    for key,value in replace_dict.items():
        mdx=mdx.replace(key,value)
    with open(mdx_name.replace('.mdx','_recover.mdx'),'w',encoding='utf-8') as f:
        f.write(mdx)
def clean(mdx_name):
    os.remove(mdx_name.replace('.mdx','_edit.mdx'))
    os.remove(hashlib.md5(mdx_name.encode(encoding='utf-8')).hexdigest()+'.json')
    os.remove(mdx_name)
    os.rename(mdx_name.replace('.mdx','_recover.mdx'),mdx_name)
if __name__=='__main__':
    translate_label(mdx_name)
    recover(mdx_name)
    clean(mdx_name)
