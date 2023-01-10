# -*- coding: utf-8 -*-
# @Time    : 2023/1/10 15:37
# @Author  : jinjie
# @File    : 12_observer_mode.py
# 观察者模式

from abc import ABCMeta, abstractmethod


# 订阅者 抽象类接口
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self,notice): #当有notice时，自动更新订阅 notice是一个Notice类（子类）对象
        pass

# 发布者 抽象类，但是方法都是实体，没有抽象方法
class Notice:
    # 发布者和订阅者可以解绑，使用列表来管理订阅者
    def __init__(self):
        self.observers = []

    # 关联订阅者
    def attach(self,obs):
        self.observers.append(obs)

    # 取消订阅者
    def detach(self,obs):
        self.observers.remove(obs)  # pop只能根据索引删除，remove根据值删除

    # 通知所有订阅者(推送方法)
    def notify(self):
        for obs in self.observers:
            obs.update(self)  # self是notice类本身,更新所有成员的订阅


# 发布者实体
class StaffNotice(Notice):
    def __init__(self,company_info=None): #company_info默认不传为None
        super().__init__() #通过父类构造init中的observers属性
        self.__company_info = company_info  #公司信息作为对象

    @property  #属性装饰器 获取私有成员变量，然后return
    def company_info(self):
        return self.__company_info

    @company_info.setter  #将info写入私有成员变量__company_info
    def company_info(self,info):
        self.__company_info = info  #将新info赋给__company_info
        self.notify()  #【最关键：赋值自动推送】推送公司信息至所有的观察者（staff）

# obj = StaffNotice("abc")  #读取
# print(obj.company_info)
# obj.company_info = "xyz"  # 赋值
# print(obj.company_info)


# 员工实体
class Staff(Observer):
    def __init__(self):
        self.company_info = None  # 自己维护当前的公司信息company_info
    def update(self,notice):
        self.company_info = notice.company_info  #将当前公司的info赋值给给staff.company_info


notice = StaffNotice("公司信息init")
# 实例化对象 观察者observer
s1 = Staff()
s2 = Staff()
# notice订阅对象staff 存入observers列表
notice.attach(s1)
notice.attach(s2)

print(s1.company_info)  # --> None #初始化时设为None
print(notice.company_info)  # --> 前面给StaffNotic初始化了一个“公司信息init”
notice.company_info = "公司第一号通知"
print("-----公司更新通知1------")
print("员工1 "+s1.company_info)
print("员工1 "+s2.company_info) # --> "公司第一号通知"信息被推送给所有用户
print("-----解绑对象2------")
# 解绑订阅对象
notice.detach(s2)
print(s2.company_info)
notice.company_info = "公司第二号通知"
print("-----公司更新通知2------")
print("员工1 "+s1.company_info)
print("员工2 "+s2.company_info)
