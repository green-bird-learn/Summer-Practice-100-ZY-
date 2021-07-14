# -*- coding: utf-8 -*-
# @Time: 2021-07-11 12:38
# @Author: little kimber
# @File: text_editor.py
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QFontDialog
from PyQt5 import uic
from PyQt5.QtCore import QFile
from PyQt5.QtGui import QIcon
import sys


class Editor():
    def __init__(self):
        self.ui = uic.loadUi("text_editor.ui")
        self.ui.open_button.clicked.connect(self.open_file)
        self.ui.save_button.clicked.connect(self.save_file)
        self.ui.clear_button.clicked.connect(self.clear_file)
        self.ui.font_button.clicked.connect(self.font_change)
        self.ui.color_button.clicked.connect(self.color_change)

    def open_file(self):
        files = QFileDialog.getOpenFileName(self.ui, "打开本地文件")
        if files[0]:
            with open(files[0], mode='r', encoding="utf-8") as f:
                self.ui.text.setText(f.read())

    def save_file(self):
        file = QFileDialog.getSaveFileName(self.ui, "保存文件")
        if file[0]:
            print(file[0])
            with open(file[0], "w") as f:
                f.write(self.ui.text.toPlainText())

    def clear_file(self):
        self.ui.text.clear()

    def font_change(self):
        fo, b = QFontDialog.getFont()
        if b:
            self.ui.text.setCurrentFont(fo)

    def color_change(self):
        co = QColorDialog.getColor()
        if co.isValid():
            self.ui.text.setTextColor(co)



app = QApplication(sys.argv)
editor = Editor()
editor.ui.show()
app.exec_()
