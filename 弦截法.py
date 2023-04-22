# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:45:37 2023

@author: 86319
"""

import math

# 定义函数 func，它接受一个参数 x，返回方程的值
def func(x):
    return x * math.cosh(50 / x) - x - 10

# 定义函数 secant，使用弦截法计算方程的根
# x0 和 x1 是起始点，tol 是所需的精度
def secant(x0, x1, tol):
    while True:
        # 计算在当前两个点 x0 和 x1 的函数值
        f0 = func(x0)
        f1 = func(x1)
        # 使用弦截法计算下一个点 x
        x = x1 - f1 * (x1 - x0) / (f1 - f0)
        # 计算新点的函数值
        fx = func(x)
        # 如果满足所需的精度，则返回近似值
        if abs(fx) < tol:
            return x
        # 否则，将 x1 的值设置为 x，将 x0 的值设置为原来的 x1
        x0 = x1
        x1 = x

# 使用 secant 函数计算方程的根
root = secant(120, 150, 0.000001)
# 打印根的近似值，保留五位小数
print("方程的根的近似值为：", round(root, 5))
