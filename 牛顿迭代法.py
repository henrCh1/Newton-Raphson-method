# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:45:36 2023

@author: 86319
"""
import math

# 定义函数f(x)，即sinx-x/2
def f(x):
    return math.sin(x) - x/2

# 定义函数f_prime(x)，即f(x)的导数
def f_prime(x):
    return math.cos(x) - 1/2

# 定义牛顿迭代法函数newton_method(x0, eps)，其中x0为起始点，eps为所需精度
def newton_method(x0, eps):
    x = x0
    # 当函数值的绝对值大于给定精度时继续迭代
    while abs(f(x)) > eps:
        # 使用牛顿迭代法更新x的值
        x = x - f(x) / f_prime(x)
    # 返回方程的正根
    return x

# 调用newton_method函数计算方程的正根，并打印结果
root = newton_method(math.pi/2, 0.0001)
print("sinx-x/2=0的正根为:", root)
