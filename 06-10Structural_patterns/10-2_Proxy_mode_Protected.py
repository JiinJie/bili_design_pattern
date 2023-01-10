# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 12:01
# @Author  : jinjie
# @File    : 10-2_Proxy_mode_Protected.py

from abc import ABCMeta,abstractmethod

# 抽象对象
class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

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


# 保护代理 -- 控制不符合条件的用户，没有写入权限
class ProtectedProxy(Subject):
    def __init__(self,filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        # if id != admin
        raise PermissionError('无写入权限！')


subj = ProtectedProxy('test.txt')
print(subj.get_content())
subj.set_content('abc')

