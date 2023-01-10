# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 16:56
# @Author  : jinjie
# @File    : 13_strategy_mode.py
# 策略模式

from abc import ABCMeta,abstractmethod

# 抽象的策略接口
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self,data):
        pass

# 策略实体
class FastStrategy(Strategy):
    def execute(self,data):
        print("速度快的策略,效果一般  %s" % data)


class SlowStrategy(Strategy):
    def execute(self,data):
        print("速度较慢的策略，效果很好  %s" % data)


# 封装策略实体的上下文
class Context:
    def __init__(self,strategy,data): #初始化传入strategy和data
        self.data = data
        self.strategy = strategy

    # 切换策略
    def set_strategy(self,strategy):
        self.strategy = strategy

    # 执行策略
    def do_strategy(self):
        self.strategy.execute(self.data)


# client
data = "位置数据&车辆数据"
sf = FastStrategy()
ss = SlowStrategy()
# 创建上下文对象，传入data和strategy
context = Context(sf,data)
context.do_strategy() # 执行策略
# 切换策略

context.set_strategy(ss)
print("----策略已切换----")
context.do_strategy() # 执行策略
