import re
def deal_with_framework(text,framework):
    codes = re.findall(r"```.*?```",text,flags=re.S)
    replace_codes=[]
    for code in codes:
        replace_codes.append('\n'.join(['```python\n#####'+framework]+code.split('\n')[1:-1])+'####end\n```')
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
'''
Sub FindAndFormat()
    '声明一个 Range 对象，用来存储查找结果
    Dim rng As Range
    '声明一个 Find 对象，用来执行查找操作
    Dim fnd As Find
    
    '设置 rng 为活动文档的范围
    Set rng = ActiveDocument.Range
    
    '设置 fnd 为 rng 的 Find 属性
    Set fnd = rng.Find
    Dim sty As Style
    
    '设置要应用的样式为“标题 1”
    Set sty = ActiveDocument.Styles("Pytorch")
    '设置查找选项，使用正则表达式和通配符
    With fnd
        .ClearFormatting '清除之前的格式设置
        .Text = "#####Pytorch.*?####end" '要查找的文本，匹配 {#if fw === ‘pt’} 和 {/if} 之间的任意内容，包括换行符
        .MatchWildcards = True '启用通配符
        .Wrap = wdFindStop '到达文档末尾时停止查找
        .Forward = True '向前查找
        .Format = False '不考虑格式
        .Execute '执行查找操作
    End With
    
    '如果找到了匹配结果，就选中并打印出来
    Do While fnd.Found
        rng.Style = sty '将 rng 的样式设置为 sty
        fnd.Execute '继续查找下一个匹配结果
    Loop
    '声明一个 Range 对象，用来存储查找结果
    Dim rng As Range
    '声明一个 Find 对象，用来执行查找操作
    Dim fnd As Find
    
    '设置 rng 为活动文档的范围
    Set rng = ActiveDocument.Range
    
    '设置 fnd 为 rng 的 Find 属性
    Set fnd = rng.Find
    Dim sty As Style
    
    '设置要应用的样式为“标题 1”
    Set sty = ActiveDocument.Styles("TensorFlow")
    '设置查找选项，使用正则表达式和通配符
    With fnd
        .ClearFormatting '清除之前的格式设置
        .Text = "#####TensorFlow.*?####end" '要查找的文本，匹配 {#if fw === ‘pt’} 和 {/if} 之间的任意内容，包括换行符
        .MatchWildcards = True '启用通配符
        .Wrap = wdFindStop '到达文档末尾时停止查找
        .Forward = True '向前查找
        .Format = False '不考虑格式
        .Execute '执行查找操作
    End With
    
    '如果找到了匹配结果，就选中并打印出来
    Do While fnd.Found
        rng.Style = sty '将 rng 的样式设置为 sty
        fnd.Execute '继续查找下一个匹配结果
    Loop
    
End Sub
'''

#####TensorFlow^l
####end