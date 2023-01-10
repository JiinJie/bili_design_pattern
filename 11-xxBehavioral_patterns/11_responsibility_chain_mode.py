# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 14:50
# @Author  : jinjie
# @File    : 11_responsibility_chain_mode.py
# 责任链模式
"""
需求：   请假天数，2天以内项目直属领导。3-5天以内部门领导审批，6-10天以内总经理审批，不允许10天以上
"""


from abc import ABCMeta,abstractmethod


# 抽象类接口
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self,day):
        pass


# 实体类
class GeneralManagerHandler(Handler):
    def handle_leave(self,day):
        if day>5 & day <=10 :
            print("总经理批准假期 %d 天" % day)
        else:
            print("总经理不批")



class DepartmentManagerHandler(Handler):
    # 链表结构给下一个对象（上级领导）操作
    def __init__(self):
        self.next = GeneralManagerHandler()

    def handle_leave(self, day):
        if day <=5:
            print("部门经理批准假期 %d 天" % day)
        else:
            print("部门经理权限不足，已向上级汇报")
            self.next.handle_leave(day)



class ProjectManagerHandler(Handler):
    # 链表结构给下一个对象（上级领导）操作
    def __init__(self):
        self.next = DepartmentManagerHandler()

    def handle_leave(self, day):
        if day <=2:
            print("项目经理批准假期 %d 天" % day)
        else:
            print("项目经理权限不足，已向上级汇报")
            self.next.handle_leave(day)


# client 不需要知道最终是谁处理，只要给链表的第一个即可
day = 7
h = ProjectManagerHandler()
h.handle_leave(day)
