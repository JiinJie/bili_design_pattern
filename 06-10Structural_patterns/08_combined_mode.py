# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 17:50
# @Author  : jinjie
# @File    : 08_combined_mode.py
# 组合模式

from  abc import ABCMeta,abstractmethod

# 抽象组件 -- 创建统一接口，让两个简单对象的属性保持一致
class Graphic(metaclass=ABCMeta):
    def draw(self):
        pass


# 叶子组件 -- 简单对象
class Point(Graphic):
    # 用x和y坐标表示
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点 (%s,%s)" % (self.x, self.y)

    def draw(self):
        print(str(self))   # 打印自身，即__str__定义的内容


class Line(Graphic):
    # 用p1和p2两个点表示
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线端 [%s to %s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 复合组件 -- 复杂对象
class Picture(Graphic):
    # 是一个树形结构，需要记录父节点和其同级的子节点即可
    def __init__(self,iterable):
        self.children = []
        for g in iterable:  #如果传入的参数是可迭代的则会自动添加进children列表
            self.add(g)

    def add(self,graphic):  #给节点添加子节点（可能为简单节点，也可能为复杂节点）
        self.children.append(graphic)

    def draw(self): #复杂图像绘制的是其子节点
        print("-----start递归复杂图形-----")
        for g in self.children:
            g.draw()  #子节点一定有draw方法，因为最低等级的点和线也有
        print("-----end递归复杂图形-----")



# 客户端client
# 简单对象的调用
l = Line(Point(1,2),Point(3,3))
print(l)

# 组合为复杂对象的调用
# 简单对象
p1 = Point(5,5)
p2 = Point(6,6)
p3 = Point(6,7)
l1 = Line(Point(3,3),Point(3,4))
l2 = Line(Point(3,4),Point(4,5))
l3 = Line(Point(7,4),Point(7,5))

# 组合复杂对象1
pic1 = Picture([p1,p2,l1,l2])
pic1.draw()

# 组合复杂对象2
pic2 = Picture([p3,l3])
pic2.draw()

# 复杂对象的组合
pic12 = Picture([pic1,pic2])
pic12.draw()
