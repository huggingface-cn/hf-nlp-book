import os
import re
fix_path='Course/publish//chapter7//'
for mdx_file in os.listdir(fix_path):
    if mdx_file.endswith('.mdx'):
        with open(fix_path+mdx_file,'r',encoding='utf-8') as f:
            text=f.read()
        md_text =re.findall(r'```.*?(.*?)```',  text, flags=re.S)
        text=re.compile(r"```.*?(.*?)```",flags=re.I|re.S).sub('＋－｜－－ｎ－－｜－＋',text)
        for code in md_text:
            text=text.replace('＋－｜－－ｎ－－｜－＋','```'+'\n'.join(["python"]+code.split('\n')[1:])+'```',1)
            # ignore_dict[f'＋－｜－－{len(ignore_dict)}－－｜－＋']=f'```{strQ2B(code)}```'
        text.replace('\n\n\n','\n\n')
        with open(fix_path+mdx_file,'w',encoding='utf-8') as f:
            f.write(text)