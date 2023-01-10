# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 10:42
# @Author  : jinjie
# @File    : 09_Appearance_mode.py
#  外观模式

# 子系统类(低级硬件)
class CPU:
    def run(self):
        print('CPU start to run...')

    def stop(self):
        print('CPU stop to run...')


class Disk:
    def run(self):
        print('Disk start to run...')

    def stop(self):
        print('Disk stop to run...')


class Memory:
    def run(self):
        print('Memory start to run...')

    def stop(self):
        print('Memory stop to run...')

# 外观--高级系统（电脑整机）
class Computer():
    def __init__(self):
        self.CPU = CPU()
        self.Disc = Disk()
        self.Member = Memory()

    def run(self): #封装
        self.CPU.run()
        self.Disc.run()
        self.Member.run()

    def stop(self):
        self.CPU.stop()
        self.Disc.stop()
        self.Member.stop()


# 客户端，高层代码
c = Computer()
c.run()  #只需要知道高级系统（外观）中的调用方法即可
print("---启动成功---")
c.stop()
print("---关闭成功---")
