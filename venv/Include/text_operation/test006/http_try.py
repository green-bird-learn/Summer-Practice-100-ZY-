# -*- coding: utf-8 -*-
# @Time: 2021-07-13 11:48
# @Author: little kimber
# @File: http_try.py
from PyQt5 import uic
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication
class HTTP:
    def __init__(self):
        self.ui = uic.loadUi(r"C:\Users\Administrator\Desktop\qss_pilot2\http.ui")

app = QApplication([])
http = HTTP()
http.ui.show()
app.exec_()