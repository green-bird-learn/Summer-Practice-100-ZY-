# -*- coding: utf-8 -*-
# @Time: 2021-07-10 10:44
# @Author: little kimber
# @File: test005.py
"""
统计字符串中的单词数目——统计字符串中单词的数目，更复杂的话从一个文本中读出字符串并生成单词数目统计结果。
思路：从外部提供一段文本再进行操作,为了简化题目，我们只输出出现频率前十的单词
"""
# 首先读取文档
def get_word():
    f = open("./target_text", encoding='utf-8')
    readline = f.readlines()
    word = []
    # 得到文章的单词并存入列表中
    for line in readline:
        line = line.replace(",", " ")
        line = line.strip()
        wo = line.split(" ")
        word.extend(wo)
    return word

def clear_count(lists):
    wokey = {}
    wokey = wokey.fromkeys(lists)  # 这一步可以去除重复的单词,下面的列表全是去重后的单词
    word_1 = list(wokey.keys())
    for i in word_1:
        wokey[i] = lists.count(i)  # 字典的键对应的值是单词的统计个数
    return wokey

def sort_list(wokey):
    del(wokey[''])
    wokey_1 = {}
    wokey_1 = sorted(wokey.items(), key=lambda d:d[1], reverse=True)
    wokey_1 = dict(wokey_1)
    return wokey_1

def main():
    word = get_word()
    wokey = clear_count(word)
    sort_wokey = sort_list(wokey)
    flag = 0
    for x, y in sort_wokey.items():
        if flag<=10:
            print(f"the word is {x}, and its amount is {y}")
            flag += 1
        else:
            break

main()
