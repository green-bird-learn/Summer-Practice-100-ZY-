# -*- coding: utf-8 -*-
# @Time: 2021-07-09 16:59
# @Author: little kimber
# @File: test001.py
"""
1.输入一个字符串，将其逆转并输出
思考：字符串在python中的类型,都有什么方法可以翻转字符串?
"""

while True:
    user_input = input("please input your test string: ")
    print(user_input[::-1])
    print("whether to stop? yes/1 no/0")
    judge = int(input("yes/no?: ")) # 这里如果不转换为int类型，则judge为‘0’，而python认为字符串为真
    if judge:
        break




