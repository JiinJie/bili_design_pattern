# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 11:05
# @Author  : jinjie
# @File    : 10-1_Proxy_mode_Virtual.py
# 代理模式--虚代理

from abc import ABCMeta,abstractmethod

# 抽象对象
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self,content):
        pass


# 实例对象
class RealSubject(Subject):
    def __init__(self,filename): #初始化读取文件内容存入content
        self.filename = filename
        print('读取文件内容！')
        with open(self.filename, 'r', encoding='utf-8') as f:
            self.content = f.read()
            print("初始化将content写入内存  "+self.content)

    def get_content(self):
        return self.content

    def set_content(self,content): # 将内容写入文件
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(content)

    def add_content(self,content):
        with open(self.filename, 'a', encoding='utf-8') as f:
            f.write(content)



subj = RealSubject('test.txt')  #读取内容时就会将content写入内存
# content = subj.get_content()
# print(content)
# # 覆盖写入
# c1 = subj.set_content(content)
# # 追加写入
# c2 = subj.add_content(content)


# 虚代理 （只有调用get_content才会将内容写入内存）

class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None #默认初始化对象时，对象属性为None

    # 默认不会占用内存，因为属性为None，当调用时才会实例化，写入内存
    def get_content(self):
        if not self.subj: #如果没有这个对象，则实例化为RealSubject
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
            return self.subj.set_content(content)

print("-"*20)
vir_subj = VirtualProxy('test.txt')
print("-"*20)
print(vir_subj.get_content()) #调用方法时才会实例化

