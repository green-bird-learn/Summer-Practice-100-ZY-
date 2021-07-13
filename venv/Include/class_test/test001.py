# -*- coding: utf-8 -*-
# @Time: 2021-07-13 9:01
# @Author: little kimber
# @File: test001.py

'''
产品库存管理——创建一个管理产品库存的应用。建立一个产品类，包含价格、id、库存数量。
然后建立一个库存类，记录各种产品并能计算库存的总价值。
'''

class Product:
    def __init__(self, index, name, value, number):
        self.value = value
        self.name = name
        self.index = index
        self.number = number

    def __str__(self):
        return f"产品名称:{self.name}, 产品价格:{self.value}, 产品编号:{self.index}, 产品数量:{self.number}"

class Storage:
    def __init__(self):
        self.goods = []

    def add(self, product):
        '''

        :param product:
        :return:
        添加产品，如果仓库总有产品，判断是否是新产品，是新产品，直接添加，不是新产品，增加数量
        如果仓库中没有产品，就直接添加
        '''
        if len(self.goods) > 0:
            flag = 0
            for i in range(len(self.goods)):
                if self.goods[i].index == product.index:
                    self.goods[i].number += product.number
                    flag = 1
                    break
                if flag != 1:
                    self.goods.append(product)
        else:
            self.goods.append(product)

    def showinfo(self):
        for i in range(len(self.goods)):
            print(self.goods[i])

    def sum(self):
        total_value = 0
        for i in range(len(self.goods)):
            total_value += self.goods[i].value*self.goods[i].number
        return total_value


p1 = Product("001", "手机", 100, 2)
store = Storage()
store.add(p1)
store.showinfo()
money = store.sum()
print(f"库存总价值为{money}")

