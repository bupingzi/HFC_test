#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:Bottle
@file:test.py
@date:2023/10/18 21:51
@desc:''
"""


class Design():
    def __init__(self, name, lower_left_x, lower_left_y, upper_right_x, upper_right_y, p_count, md5_sum):
        self.name = name
        self.lower_left_x = lower_left_x
        self.lower_left_y = lower_left_y
        self.upper_right_x = upper_right_x
        self.upper_right_y = upper_right_y
        self.p_count = p_count
        self.md5_sum = md5_sum
        # self.area = area #面积计算未编写，由于没理解具体是什么面积，所以只搭了框架
        self.density = self.get_density()

    def get_density(self):  # 计算密度。同上面，没有准确的密度计算公式，因此只是简单的/100，方便后面调用输出
        return int(self.p_count)/100


class Library():
    def __init__(self, design_list):
        super().__init__()
        self.design_list = design_list

    def print_desity(self): #实现排序
        return sorted(self.design_list, key=lambda item:item.density,reverse=True)


test_data = []  # 列表存放数据
for line in open('testdata.txt', 'r+'):  # 读取数据，并分割添加到test_data中
    line_text = line.split('\t')
    test_data.append(line_text)
design_list = []  # 遍历test_data中数据
for index, _data in enumerate(test_data):
    if index == 0:  # 跳过首行标题
        continue
    design = Design(name=_data[0], lower_left_x=_data[1], lower_left_y=_data[2], upper_right_x=_data[3],
                    upper_right_y=_data[4], p_count=_data[5], md5_sum=_data[6])
    design_list.append(design)
lib = Library(design_list)  # 调用Library
res = lib.print_desity()  #调用print_desity方法，实现排序
for _res in res:   # 打印结果
    print(_res.name,' ',_res.density)
