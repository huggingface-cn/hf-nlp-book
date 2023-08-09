import re
def deal_with_framework(text,framework):
    codes = re.findall(r"```.*?```",text,flags=re.S)
    replace_codes=[]
    for code in codes:
        replace_codes.append('\n'.join(['```{.'+framework+'}']+code.split('\n')[1:]))
    for code_index in range(len(codes)):
        text=text.replace(codes[code_index],replace_codes[code_index])
    return text
file_name='Course\publish\第八章 掌握主要的 NLP 任务\第八章.mdx'
mdx=open(file_name,'r',encoding='utf-8').read()
spaces = re.findall(r"\{#if fw === '.*?'\}.*?\{/if\}",mdx,flags=re.S)
repace_space=[]
for space in spaces:
    if '{:else}' not in space:
        if 'tf' in space[:15]:
            repace_space.append(deal_with_framework(space,"TensorFlow"))
        elif 'pt' in space[:15]:
            repace_space.append(deal_with_framework(space,"Pytorch"))
    else:
        space_split=space.split('{:else}')
        if 'tf' in space_split[0][:15]:
            repace_space.append(deal_with_framework(space_split[0],"TensorFlow")+'{:else}'+deal_with_framework(space_split[1],"Pytorch"))
        if 'pt' in space_split[0][:15]:
            repace_space.append(deal_with_framework(space_split[0],"Pytorch")+'{:else}'+deal_with_framework(space_split[1],"TensorFlow"))
for space_index in range(len(spaces)):
    mdx=mdx.replace(spaces[space_index],repace_space[space_index])
open(file_name.split('.')[0]+'_fix.mdx','w',encoding='utf-8').write(mdx)