# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 11:14
# @Author  : jinjie
# @File    : 03-2_factory_method.py
# 工厂方法模式

from abc import ABCMeta,abstractmethod


class Payment(metaclass=ABCMeta):
    # abc --> abstract class
    @abstractmethod
    def pay(self,money):
        pass


class Alipay(Payment):
    def __init__(self,use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        # 如果传参为True则会执行use_huabei条件的操作
        if self.use_huabei:
            print("花呗支付成功 %d 元" % money)
        else:
            print("支付宝支付成功 %d 元" % money)

class Wechatpay(Payment):
    def pay(self,money):
        print("微信支付成功 %d 元" % money)

# 添加新功能已经解耦
class Bankpay(Payment):
    def pay(self,money):
        print("网上银行支付成功 %d 元" % money)


#创建抽象工厂接口约束工厂类
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

# 创建工厂类实例
class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatFactory(PaymentFactory):
    def create_payment(self):
        return Wechatpay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)

# 添加新功能
class BankFactory(PaymentFactory):
    def create_payment(self):
        return Bankpay()


# client
pf = HuabeiFactory()
p = pf.create_payment()
p.pay(66)


pf2 = BankFactory()
p2 = pf2.create_payment()
p2.pay(88)







