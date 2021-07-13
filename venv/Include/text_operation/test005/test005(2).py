# -*- coding: utf-8 -*-
# @Time: 2021-07-10 11:37
# @Author: little kimber
# @File: test005(2).py

from collections import Counter
import re

cnt = Counter()

f = open("./target_text", encoding='utf=8')
for w in f:
    w = w.lower()
    # 正则表达式替换特殊字符
    # w = w.replace("\n","");
    w = re.sub("[!,\n]", "", w)
    w.strip()
    for word in w.split(" "):
        cnt[word] += 1

print(cnt)
