# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 17:20
# @Author  : jinjie
# @File    : 14_template_method_mode.py
# 模板方法模式

from abc import ABCMeta,abstractmethod
from time import sleep


# 抽象类:定义3个抽象方法，1具体方法
class Window(metaclass=ABCMeta):
    # 抽象方法 -- 原子操作（钩子操作）【可变内容】
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def repaint(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # 具体方法 -- 模板方法 【基本框架流程】
    def run(self):
        while True:
            try:
                self.repaint()
                sleep(1)  #间隔1秒重新绘制窗口
            except KeyboardInterrupt: #关闭时触发异常，退出循环
                break
        self.stop() #执行退出操作

# 具体类
class MyWindow(Window):
    def __init__(self,msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口已关闭")

    def repaint(self):
        print("窗口已重新绘制，原因： %s" % self.msg)


# client
MyWindow("用户点击操作").run()
