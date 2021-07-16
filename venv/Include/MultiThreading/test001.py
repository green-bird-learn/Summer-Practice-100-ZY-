# -*- coding: utf-8 -*-
# @Time: 2021-07-15 16:44
# @Author: little kimber
# @File: test001.py
'''
下载进度条——创建一个表示下载进度的进度条。进度条由独立的线程操作，通过委托来和主线程进行通讯。
'''

import requests
from tqdm import tqdm

def download(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"
    }
    filename = url.split("/")[-1]
    print("正在下载文件...")
    head = requests.head(url, headers=headers)
    file_size = int(head.headers.get("Content-Length"))
    chunk_size = 1024  # 每次读取的大小
    read = 0  # 已经读入的大小
    response = requests.get(url, headers=headers, stream=True)
    bar = tqdm(total=file_size, desc=f"下载文件{filename}")
    with open(filename, mode="wb") as f:
        for chunk in response.iter_content(chunk_size=chunk_size):
            f.write(chunk)
            bar.update(chunk_size)
    bar.close()

if __name__ == '__main__':
    url = 'https://issuecdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.2.8.9.exe'
    download(url=url)
