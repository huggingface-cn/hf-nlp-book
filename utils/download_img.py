import os
import requests
import re
import warnings
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# 你的文件夹路径
directory = 'Course\publish\chapter7'
if 'assets' not in os.listdir(directory):
    os.makedirs(os.path.join(directory, 'assets'))
for filename in os.listdir(directory):
    if filename.endswith(".md") or filename.endswith(".mdx"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r+', encoding='utf8') as file:
            content = file.read()

            # 找到所有的图片链接
            img_urls = re.findall(r'\!\[.*?\]\((.*?)\)', content)

            for url in img_urls:
                if url.startswith('http'):
                    url=url.split('"')[0].strip()
                    # 解析url以获取文件名
                    a = urlparse(url)
                    img_name = os.path.basename(a.path)

                    # 下载图片
                    session = requests.Session()
                    proxies = {'http':'http://localhost:8466', 'https': 'https://localhost:8466'}
                    session.proxies = proxies
                    session.trust_env = False
                    try:
                        response = session.get(url)
                        response.raise_for_status()  # 如果HTTP请求返回了不成功的状态码, Response.raise_for_status()会抛出一个HTTPError异常
                        img_data = response.content
                        if img_data == b'':
                            raise ValueError("No data received for the url.")
                    except (requests.RequestException, ValueError) as e:
                        warnings.warn(f"{filename}:Can't download the image from {url}, it will not be replaced. Error: {str(e)}")
                        continue  # 如果图片下载失败，跳过这个图片

                    # 保存图片
                    with open(os.path.join(directory, 'assets', img_name.split(' ')[0]), 'wb') as handler:
                        handler.write(img_data)

                    # 用本地链接替换远程链接
                    content = content.replace(url, f'./assets/{img_name}')

            # 将修改后的内容写回文件
            file.seek(0)
            file.write(content)
            file.truncate()
