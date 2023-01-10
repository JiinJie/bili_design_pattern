# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 14:53
# @Author  : jinjie
# @File    : 04_builder_mode.py
#  建造者模式

from abc import ABCMeta,abstractmethod

# 定义一个基础player的属性
class Player:
    def __init__(self,face=None,body=None,arm=None,leg=None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s,%s,%s,%s" %(self.face,self.body,self.arm,self.leg)

# 抽象一个建造者类
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

class SexgirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()  # 初始化为None,否则不赋初值会报错

    def build_face(self):
        self.player.face = "good face"

    def build_body(self):
        self.player.body = "good body"

    def build_arm(self):
        self.player.arm = "good arm"

    def build_leg(self):
        self.player.leg = "good leg"


# 定义一个monster继承基础的player
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "monster face"

    def build_body(self):
        self.player.body = "monster body"

    def build_arm(self):
        self.player.arm = "monster arm"

    def build_leg(self):
        self.player.leg = "monster leg"

# 建造者导演，控制角色生成的顺序[先有躯干再有其他]
class PlayerDirector:
    # 定义player的属性
    def build_player(self,builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player  #按顺序组装完成后返回该player


# client
builder1 = SexgirlBuilder()      # 创建player对象即属性
director = PlayerDirector()     # 创建建造者导演对象
p1 = director.build_player(builder1)  # 实例化对象
print(p1)


builder2 = MonsterBuilder()
p2 = director.build_player(builder2)
print(p2)
