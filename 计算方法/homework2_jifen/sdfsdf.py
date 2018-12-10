# coding:utf-8
import numpy as np
import math
# 定义复合辛普森的算法

f3 = lambda i:i**(3.0/2)

def trapezoid(l1,l2):
    h = (l1[-1]-l1[0])/(len(l1)-1)
#     print(h,"\n")
    sum = 0.0
    for i in range(1,len(l1)-1): # 注意这里是len(l1)-1的啊。
#         print(l2[i])
        sum +=2.0*l2[i]
    return 1.0*h/2*(l2[0]+l2[-1]+sum)


def extrapolation(a,b,m,k):

#     print inner_l1,"\n",inner_l2
    if m==0:
        number = 2 ** k + 1
        inner_l1 = list(np.linspace(a, b, number))
        inner_l2 = [f3(x) for x in inner_l1]
        return trapezoid(inner_l1,inner_l2)
    else:
        # return 1.0*(4**m)/(4**m-1)*extrapolation(a,b,m-1,k+1)-(1.0/(4**m)-1)*extrapolation(a,b,m-1,k)
        pre = 1.0*4**m/(4**m-1)
        las = 1.0/(4**m-1)
        pre_result = extrapolation(a,b,m-1,k+1)
        las_result = extrapolation(a,b,m-1,k)
        return pre*pre_result-las*las_result


# 定义了截断的小数
def floor(x,n):
    return math.floor(x*10**n)/(10**n)


print extrapolation(0,1,2,1)
