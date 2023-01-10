# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 9:50
# @Author  : jinjie
# @File    : 01_abstract_class.py

from abc import ABCMeta,abstractmethod

# 如果一个类有抽象方法那他就是个抽象类
class Payment(metaclass=ABCMeta):
    # abc --> abstract class

    # pay就是一个抽象方法的集合,通过@bstractmethod装饰器，赋予其相应属性
    @abstractmethod
    def pay(self,money):
        pass

# alipay 继承抽象类Payment
#class Alipay(Payment):
    #pass
    # -->TypeError: Can't instantiate abstract class Alipay with abstract method pay
    # 直接使用会报错，因为无法实例化抽象类，只有实现了抽象类中的抽象方法才可以使用

#p1 = Alipay()

class Wechatpay(Payment):
    # 实现同名的抽象方法
    def pay(self,money):
        print("支付成功 %d 元" % money)


p2 = Wechatpay()
p2.pay(50)



