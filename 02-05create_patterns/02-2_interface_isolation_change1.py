# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 10:37
# @Author  : jinjie
# @File    : 02-2_interface_isolation_org.py
# 接口隔离原则修改版

from abc import ABCMeta,abstractmethod

# 接口隔离，使用多个专门的接口
class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        print("can walk")

class WaterAnmal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        print("can swim")

class SkyAnmal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        print("can fly")


class Tiger(LandAnimal):
    def walk(self):
        print("tiger can walk")

# 使用多继承抽象接口
class Frog(LandAnimal,WaterAnmal):
    def walk(self):
        print("frog can walk")

    def swim(self):
        print("frog can swim")

