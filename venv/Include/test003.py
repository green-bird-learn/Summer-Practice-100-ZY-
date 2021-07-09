# -*- coding: utf-8 -*-
# @Time: 2021-07-09 18:37
# @Author: little kimber
# @File: test003.py
"""
统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
"""
def create_string():
    string = input("please input the targeted string: ")
    return string

def Count(string):
    result = 0
    vowel = 'aeiouAEIOU'
    for v in vowel:
        result += string.count(v)
    return result

while True:
    sentence = create_string()
    print(f"the number of vowel letter in the sentence is {Count(sentence)}")
    judge = input("whether to stop yes:1 no :0")
    if judge:
        break