# -*- coding: utf-8 -*-
# @Time: 2021-07-09 17:11
# @Author: little kimber
# @File: test002.py
"""
拉丁猪文字游戏——这是一个英语语言游戏。
基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾并
且加上后缀-ay（譬如“banana”会变成“anana-bay”）。
可以在维基百科上了解更多内容。
"""
def create_words():
    origin_word = input("please input your original words: ")
    return origin_word

def Game(words):
    for letter in words:
        if letter not in "aeiou":
            result_word = change(letter, words)
            print(result_word)
            break
        else:
            pass

def change(letter, words):
    pos = words.index(letter)
    return words[:pos]+words[pos+1:]+"-"+letter+"ay"

while True:
    words = create_words()
    Game(words)
    judge = int(input("Quit the game? yes:1 no:0"))
    if judge:
        break