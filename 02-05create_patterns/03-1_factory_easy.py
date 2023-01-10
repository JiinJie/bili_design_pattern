# -*- coding: utf-8 -*-
# @Time    : 2023/1/9 11:14
# @Author  : jinjie
# @File    : 03-1_factory_easy.py
# 简单工厂模式

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

# 创建工厂模式类
class PaymentFactory:
    def create_payment(self,method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechatpay':
            return Wechatpay()
        # 直接修改功能，高层模块不需要知道内部调用情况
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            # 都不存在则抛出异常
            raise TypeError("No such class named %s" % method)



# 创建client使用工厂类
pf = PaymentFactory()
p3 = pf.create_payment('alipay')
p3.pay(100)

p4 = pf.create_payment('huabei')
p4.pay(66)




