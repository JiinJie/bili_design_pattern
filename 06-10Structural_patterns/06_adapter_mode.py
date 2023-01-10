# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 16:21
# @Author  : jinjie
# @File    : 06_adapter_mode.py
# 适配器模式

from abc import ABCMeta,abstractmethod


class Payment(metaclass=ABCMeta):
    # abc --> abstract class
    @abstractmethod
    def pay(self,money):
        pass

# 系统一
class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付成功 %d 元" % money)

class Wechatpay(Payment):
    def pay(self,money):
        print("微信支付成功 %d 元" % money)

# 系统二
class Bankpay:
    def cost(self,money):
        print("银联支付成功 %d 元" % money)

class Applepay:
    def cost(self,money):
        print("苹果支付成功 %d 元" % money)


# 添加“类适配器”：兼容系统一和系统 二
class NewBankPay(Payment,Bankpay):
    def pay(self,money):
        self.cost(money) #将cost外面套壳为pay

# 添加“对象适配器”：当有多个系统时，需要继承多个类，比较繁琐。因此使用"组合"方法：
# 组合： 在一个类中放入其他类对象
class PaymentAdapter:
    #初始化一个payment对象
    def __init__(self, payment):
        self.payment = payment

    def pay(self,money):
        # 定义pay方法，执行：让payment引用cost方法
        self.payment.cost(money)



# 方法一：client
p = NewBankPay()
p.pay(100)

# 方法二：client
p2 = PaymentAdapter(Bankpay())
p2.pay(88)
p3 = Alipay()
p3.pay(66)


# "组合"实例:
# class A:
#     pass
#
# class B:
#     def __int__(self):
#         self.a = A()

