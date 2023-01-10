# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 17:02
# @Author  : jinjie
# @File    : 07_bridge_mode.py
# 桥接模式

from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    # 初始化，传入color
    def __init__(self,color):
        self.color = color

    @abstractmethod
    def draw(self): #draw一个shape
        pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self,shape): #paint给shape着色
        pass

# 长方形类
class Rectangle(Shape):
    name = "长方形"
    def draw(self):
        # 画长方形逻辑
        self.color.paint(self) #panint需要一个shape，此时self就是draw的shape，直接传入即可


# 圆形类
class Circle(Shape):
    name = "圆形"
    def draw(self):
        # 画圆形逻辑
        self.color.paint(self)

# 新增一个三角形类
class Triangle(Shape):
    name = "三角形"
    def draw(self):
        # 画三角形逻辑
        self.color.paint(self)



# 红色类
class Red(Color):
    def paint(self,shape):
        print("红色的%s" % shape.name)

class Green(Color):
    def paint(self,shape):
        print("绿色的%s" % shape.name)


# client
shape1 = Rectangle(Red()) #创建一个红色的长方形对象。 传入的Red()是个对象，即在对象中传入对象
shape1.draw()  #调用函数，创建实例
# -->红色的长方形

shape2 = Triangle(Green())
shape2.draw()

