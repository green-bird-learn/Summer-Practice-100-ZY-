# -*- coding: utf-8 -*-
# @Time: 2021-07-13 11:48
# @Author: little kimber
# @File: http_try.py
from PyQt5 import uic
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
class HTTP:
    def __init__(self):
        self.ui = uic.loadUi(r".\http.ui")

app = QApplication([])
app.setWindowIcon(QIcon("icons8-aliexpress-100.png"))
http = HTTP()
http.ui.show()
app.exec_()