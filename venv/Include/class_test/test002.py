# -*- coding: utf-8 -*-
# @Time: 2021-07-13 17:01
# @Author: little kimber
# @File: test002.py
"""
电影商店——管理录像带租借，记录借出时间、到期时间、逾期费用。复杂一点可以生成逾期用户的账号报告。
建立四个类，分别是录像带，商店，租借人，被租借的录像带
"""

class Vedio:
    def __init__(self, price, number, name, id):
        self.price = price
        self.number = number
        self.id = id
        self. name = name

    def __str__(self):
        return f"名称：{self.name},数量:{self.number},价格:{self.price},类别编号:{self.id}"

class Borrow_vedio:
    def __init__(self, borrow_name, borrow_id, user_id, borrow_day, back_day, today, due_day):
        self.borrow_name = borrow_name
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.borrow_day = borrow_day
        self.back_day = back_day
        self.today = today
        self.due_day = due_day

    def __str__(self):
        return f'''被租借的录像带： 名称：{self.borrow_name}, 编号:{self.borrow_id} 
                租借人编号:{self.user_id}
                租借日期:{self.borrow_day}, 应还日期:{self.back_day}
                已逾期:{self.due_day}
                '''

class User:
    def __init__(self, name, u_id):
        self.name = name
        self.u_id = u_id
        self.borrowed = []

    def __str__(self):
        return f"用户姓名:{self.name}, 用户编号:{self.u_id}"

    def borrow(self, vedio, flag=1):
        # 设定最多借5个录像带
        if(len(self.borrowed)<5 or flag==0):
            if flag == 1:
                self.borrowed.append(vedio)
            else:
                self.borrowed.remove(vedio)

        else:
            print("已经超出借阅数量，不能再借阅")

    def n_vedio(self):
        return len(self.borrowed)

    def list_vedio(self):
        for vedio in self.borrowed:
            print(vedio)

class Shop:
    def __init__(self):
        self.vedio = []
        self.borrowed_vedio = []
        self.user = []
        self.overdue = []
        self.due_day = 30

    def addVedio(self, vedio_tape):
        if len(self.vedio) > 0:
            flag = 0
            for v in self.vedio:
                if v.name == vedio_tape.name and v.id == vedio_tape.id:
                    v.number += vedio_tape.number
                    flag = 1
            if flag != 1:
                self.vedio.append(vedio_tape)
        else:
            self.vedio.append(vedio_tape)

    def delVedio(self, vedio_tape):
        flag = 0
        for v in self.vedio:
            if v.name == vedio_tape.name and v.id == vedio_tape.id:
                flag = 1
                if v.number > vedio_tape.number:
                    v.number -= vedio_tapenumber
                elif v.number == vedio_tape.number:
                    self.vedio.remove(v)
                else:
                    print("录像带数量不足")
                break
        if flag == 0:
            print("未找到该录像带")

    def findVedio(self, key):
        if isinstance(key, int):
            flag = 0
            for v in self.vedio:
                if v.id == key:
                    flag = 1
                    print(v)
                    for bor in self.borrowed_vedio:
                        if bor.id == v.id:
                            print(bor)
                break
            if flag == 0:
                print("未找到录像带")

        else:
            for v in self.vedio:
                if v.name == key:
                    flag = 1
                    print(v)
                    for bor in self.borrowed_vedio:
                        if bor.name == v.name:
                            print(bor)

    def addUser(self, user_name):
        u = User(user_name, len(self.user)+1)
        self.user.append(u)

    def findUser(self, key):
        flag = 0
        if isinstance(key, int):
            for user in self.user:
                if user.u_id == key:
                    flag = 1
                    print(user)
            if flag == 0:
                print("没有该用户")
        else:
            for user in self.user:
                if user.name == key:
                    flag = 1
                    print(user)
            if flag == 0:
                print("没有该用户")

    def borrowVedio(self, vedio, user_id, day):
        pass

    def returnVedio(self, vedio, user_id, day):
        pass

    def list_user(self):
        for user in self.user:
            print(user)

    def list_vedio(self):
        for vedio in self.vedio:
            print(vedio)

    def list_borrowed_vedio(self):
        for bor in self.borrowed_vedio:
            print(bor)

    def overdue_update(self, day):
        pass

    def overdue_report(self, day):
        pass
