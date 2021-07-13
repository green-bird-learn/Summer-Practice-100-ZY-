# -*- coding: utf-8 -*-
# @Time: 2021-07-10 10:37
# @Author: little kimber
# @File: test004.py
"""
判断是否为回文——判断用户输入的字符串是否为回文。回文是指正反拼写形式都是一样的词，譬如“racecar”。
"""
def create_string():
    string = input("pleasr input your string: ")
    return string

def judge(string):
    if string == string[::-1]:
        return True
    else:
        return False

while True:
    string = create_string()
    if judge(string):
        print("是回文数")
    else:
        print("不是回文数")
    flag = int(input("shall we continue? yes:1 no:0"))
    if not flag:
        break
