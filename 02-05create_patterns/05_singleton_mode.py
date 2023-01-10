# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 15:28
# @Author  : jinjie
# @File    : 05_singleton_mode.py
# 单例模式

# ######  方法一：使用__new__  #######
from abc import ABCMeta, abstractmethod

# 基类
class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"_instance"):
            # 如果Singleton没有_instance属性，则调用他的父类(基类)object的new方法，将myclass传入，来返回一个myclass的实例
            cls._instance = super(Singleton,cls).__new__(cls)
            # 将Myclass类的_instance返回
        return cls._instance

class Myclass(Singleton):
    def __init__(self,a):
        self.a = a

a = Myclass(10)
b = Myclass(20)

print(a.a)
print(b.a)
print(id(a),id(b))

# 两个返回的都是20，因为a和b指向了同一个实例
# --> 20
# --> 20

# 单例模式使用场景:日志记录,数据库连接器