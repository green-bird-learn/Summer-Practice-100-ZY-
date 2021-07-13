# -*- coding: utf-8 -*-
# @Time: 2021-07-11 12:38
# @Author: little kimber
# @File: text_editor.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox


class Editor():
    def __init__(self):
        # 初始化界面
        self.window = QMainWindow()
        self.window.resize(600, 300)
        self.window.move(310, 300)
        self.window.setWindowTitle("阿庄文本编辑器")

        self.textEdit = QPlainTextEdit(self.window)
        self.textEdit.setPlaceholderText("请输入文本")
        self.textEdit.move(20, 50)
        self.textEdit.resize(400, 200)

        self.button1 = QPushButton("打开", self.window)
        self.button1.clicked.connect(Open)

        self.button2 = QPushButton("编辑", self.window)
        self.button2.move(120, 0)
        self.button2.clicked.connect(Edit)

        self.button3 = QPushButton("保存", self.window)
        self.button3.move(240, 0)
        self.button3.clicked.connect(Save)

    def Open(self):
        pass

    def Edit(self):
        pass

    def Save(self):
        pass

app = QApplication([])
editor = Editor()
editor.window.show()
app.exec_()
