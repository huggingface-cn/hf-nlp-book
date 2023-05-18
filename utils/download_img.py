import os
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# 你的文件夹路径
directory = 'Course\publish\chapter1'

for filename in os.listdir(directory):
    if filename.endswith(".md") or filename.endswith(".mdx"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r+', encoding='utf8') as file:
            content = file.read()

            # 找到所有的图片链接
            img_urls = re.findall(r'\!\[.*?\]\((.*?)\)', content)

            for url in img_urls:
                if url.startswith('http'):
                    # 解析url以获取文件名
                    a = urlparse(url)
                    img_name = os.path.basename(a.path)

                    # 下载图片
                    session = requests.Session()
                    session.trust_env = False
                    img_data=response = session.get(url).content
                    while img_data == b'':
                        img_data=response = session.get(url).content
                        print('retrying',url)
                    # img_data = requests.get(url).content
                    with open(os.path.join(directory, 'assets', img_name.split(' ')[0]), 'wb') as handler:
                        handler.write(img_data)

                    # 用本地链接替换远程链接
                    content = content.replace(url, f'./assets/{img_name}')

            # 将修改后的内容写回文件
            file.seek(0)
            file.write(content)
            file.truncate()
