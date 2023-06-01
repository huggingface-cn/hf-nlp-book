import re
import os

def extract_img_html_from_markdown(markdown):
    html_pattern = r'(<div class="flex justify-center">(?:\s*<img.*?>)*\s*</div>)'
    img_pattern = r'<img[^>]*src="(.*?)" alt="(.*?)"[^>]*\/?>'
    img_block_dark_hidden_pattern = r'<img class="block dark:hidden"[^>]*src="(.*?)" alt="(.*?)"[^>]*\/?>'
    
    div_matches = re.findall(html_pattern, markdown, re.DOTALL)
    for div in div_matches:
        img_matches = re.findall(img_pattern, div, re.DOTALL)
        img_block_dark_hidden_matches = re.findall(img_block_dark_hidden_pattern, div, re.DOTALL)
        
        # If there's only one image, ignore the class attribute
        if len(img_matches) == 1:
            src, alt = img_matches[0]
            markdown_img = f'![{alt}]({src})'
            markdown = markdown.replace(div, markdown_img)
        # If there are two images, one with class="block dark:hidden" and the other with class="hidden dark:block"
        elif len(img_matches) == 2 and len(img_block_dark_hidden_matches) == 1:
            src, alt = img_block_dark_hidden_matches[0]
            markdown_img = f'![{alt}]({src})'
            markdown = markdown.replace(div, markdown_img)
    return markdown

def translate_label(input_path,output_path):
    single_label_type=['FrameworkSwitchCourse','DocNotebookDropdown','Youtube','CourseFloatingBanner']
    # mutiply_label_type=['Tip']
    mutiply_label_type=['iframe']
    label_mask_list=[]
    with open(input_path,'r',encoding='utf-8') as f:
        mdx=f.read()
    # 去除不必要的html标签
    for label in single_label_type:
        label_mask_list+=re.findall(f'< *{label}.*?/>',mdx,re.S)
    for label in mutiply_label_type:
        # label_mask_list+=re.findall(f'',mdx,re.S)
        label_mask_list+=re.findall(f'< *{label}.*?>.*?</ *{label}>.*?',mdx,re.S)
    for p in re.findall(f'(#.*)(\[\[[^\]]*\D[^\]]*\]\])',mdx):
        mdx=mdx.replace(p[0]+p[1],p[0])
    for label in label_mask_list:
        mdx=mdx.replace(label,'')
    # 将Tip标签转换，方便后续处理
    tip_mask_list=re.finditer('< *Tip.*?>',mdx,re.S)
    replace_dict={}
    replace_list=[]
    for idx,label in enumerate(tip_mask_list):
        if '✏️' in mdx[label.regs[0][0]:label.regs[0][0]+50]:
            replace_dict[f'||++==--{idx}++==--||']='<div custom-style="Tip-green">\n'
        elif '⚠️' in mdx[label.regs[0][0]:label.regs[0][0]+50]:
            replace_dict[f'||++==--{idx}++==--||']='<div custom-style="Tip-yellow">\n'
        else:
            replace_dict[f'||++==--{idx}++==--||']='<div custom-style="Tip-green">\n'
        # mdx=mdx.replace(mdx[label.regs[0][0]:label.regs[0][1]],f'||++==--{idx}++==--||')
        replace_list.append([f'||++==--{idx}++==--||',mdx[label.regs[0][0]:label.regs[0][1]]])
    for label in replace_list:
        mdx=mdx.replace(label[1],label[0],1)
    for label in replace_dict:
        mdx=mdx.replace(label,replace_dict[label])
    label_mask_list=re.findall(f'</ *Tip>',mdx,re.S)
    for idx,label in enumerate(label_mask_list):
        # replace_dict[f'||++==--{idx}++==--||']=label
        # mdx=mdx.replace(label,f'||++==--{idx}++==--||')
        mdx=mdx.replace(label,'</div>')
    #添加将html的img标签转换为Markdown的代码
    mdx = extract_img_html_from_markdown(mdx)
    #处理图片的引用的题注
    pattern = r'!\[(.*?)\]\((.*?)\)'
    replacement = r'![\1](\2 "\1")'
    mdx = re.sub(pattern, replacement, mdx)
    pattern = r'!\[(.*?)\]\((.*?)( ".*?")+'
    replacement = r'![\1](\2 "\1"'
    mdx = re.sub(pattern, replacement, mdx)
    #对于异常空行的处理
    # mdx=mdx.replace('\n\n\n','\n\n').replace('\n\n\n','\n\n')
    with open(output_path,'w',encoding='utf-8') as f:
        f.write(mdx)
basic_input_dir='Course/zh-CN/chapter2/'
basic_output_dir='Course/publish/chapter2/'
for file_name in os.listdir(basic_input_dir):
    if file_name.endswith('.mdx') and  file_name in [str(i)+'.mdx' for i in range(8)]:
        translate_label(basic_input_dir+file_name,basic_output_dir+file_name)
