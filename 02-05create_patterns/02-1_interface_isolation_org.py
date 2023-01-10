# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 10:37
# @Author  : jinjie
# @File    : 02-1_interface_isolation_org.py
# 接口隔离原则

from abc import ABCMeta,abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        print("can walk")

    @abstractmethod
    def swim(self):
        print("can swim")

    @abstractmethod
    def fly(self):
        print("can fly")


class Tiger(Animal):
    def walk(self):
        print("tiger can walk")