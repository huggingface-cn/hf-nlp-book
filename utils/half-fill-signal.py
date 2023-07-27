import re

def remove_markdown(text):
    # 去除代码块
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # 去除行内代码
    text = re.sub(r'`.*?`', '', text)
    
    # 去除HTML标签
    text = re.sub(r'<.*?>', '', text)
    
    # 去除标题
    text = re.sub(r'#+\s+', '', text)
    
    # 去除链接
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    
    # 去除图片链接
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    
    return text

def replace_symbols(text):
    # 将半角符号和英文符号替换为中文全角符号
    symbols_map = {
        '!': '！',
        '?': '？',
        ',': '，',
        '.': '。',
        ':': '：',
        ';': '；',
        '@': '＠',
        '#': '＃',
        '$': '＄',
        '%': '％',
        '&': '＆',
        '*': '＊',
        '(': '（',
        ')': '）',
        '[': '【',
        ']': '】',
        '{': '｛',
        '}': '｝',
        '<': '《',
        '>': '》',
        '|': '｜',
        '\\': '＼',
        '/': '／',
        '=': '＝',
        '+': '＋',
        '-': '－',
        '_': '＿',
        '`': '‘',
        '~': '～',
        '\'': '’',
        '\"': '“',
    }
    
    for symbol, replacement in symbols_map.items():
        text = text.replace(symbol, replacement)
    
    return text

def restore_removed_parts(text, removed_parts):
    # 还原去除的部分
    for part in removed_parts:
        text = text.replace('[removed]', part, 1)
    
    return text

# 示例用法
markdown_text = '''
# 标题

这是一段正文，包含代码块和行内代码：`print('Hello, World!')`

这是一个链接：[Google](https://www.google.com)

这是一个图片链接：![Image](https://example.com/image.jpg)

这是一段被代码块、行内代码、链接和图片链接去除后的正文。

另外，这是一段包含半角符号和英文符号的正文: !?.,:;@#$%&*()[]{}<>|\/=+-_`~'"

这是一段还原去除的部分后的正文。
'''

# 去除Markdown标记
removed_parts = re.findall(r'\[removed\]', markdown_text)
markdown_text = remove_markdown(markdown_text)

# 将剩余的正文的半角符号和英文符号转化为中文全角符号
markdown_text = replace_symbols(markdown_text)

# 还原去除的部分
markdown_text = restore_removed_parts(markdown_text, removed_parts)

print(markdown_text)
