from func import f
from trapezoid import trapezoid
from simpthon import simpthon
from extrapolate import extrapolate
from Gaussion_cumulate import Gaussion_cumulate
import numpy as np
import matplotlib.pyplot as plt
cumulater = trapezoid(0, 1,f)
print('公式化_矩形')
print(cumulater.cal(10))
# 公式化实现的矩形
cumulater = simpthon(0, 1,f)
print('公式化_辛普森')
print(cumulater.cal(10))
# 公式化实现的辛普森

cumulater = extrapolate(0,1,f)
# 外推法求解
print('外推_辛普森')
print(cumulater.degree_cal(10,1))
print('外推_科斯特')
print(cumulater.degree_cal(10,2))
print('外推_龙格')
print(cumulater.degree_cal(10,3))
# 0阶矩形，1阶辛普森，3阶龙格

cumulater = Gaussion_cumulate(0,1,f)
print('高斯_勒得让')
print(cumulater.cal(4))
# 高斯勒得让
