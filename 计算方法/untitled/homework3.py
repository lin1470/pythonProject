#coding:utf-8
import numpy as np
# import math


class iteration():
    def __init__(self,n):
        self.A = None
        self.b = None
        self.x0 = None
        self.initialization(n)

    # 构造迭代矩阵An和初始值x0 和bn。
    def initialization(self, n):
        self.b = range(1, n + 1)
        self.A = []
        self.x0 = np.zeros((n,))
        for i in range(n):
            list = range(1, n + 1)
            list[i] = n ** 2
            self.A.append(list)

    #         return self.An,self.bn,self.x0

    # 由A的矩阵分解得到LU两个矩阵。
    def LU_decompose(self,A):
        length = len(A)
        print length
        L = np.zeros((length, length))
        U = np.zeros((length, length))
        #     print L.dtype,U.dtype
        # 初始化向量
        for i in range(len(A)):
            U[0][i] = A[0][i]
            L[i][0] = A[i][0] * 1.0 / U[0][0]
        for r in range(1, len(A)):
            for i in range(r, len(A)):
                sum1 = 0
                sum2 = 0
                for k in range(0, r):
                    sum1 += L[r][k] * U[k][i]
                    sum2 += L[i][k] * U[k][r]
                U[r][i] = A[r][i] - sum1
                L[i][r] = (A[i][r] - sum2) * 1.0 / U[r][r]
        return L, U

    def LU_solve(self):
        L,U = self.LU_decompose(self.A)
        length = len(L)
        y = np.array([0.0] * length)
        x = np.array([0.0] * length)
        # print x.dtype, y.dtype
        n = len(x) - 1
        #     print len(y)
        y[0] = self.b[0]
        for i in range(1, len(y)):
            sum1 = 0
            for k in range(0, i):
                sum1 += L[i, k] * y[k] * 1.0
            y[i] = self.b[i] - sum1
        x[n] = y[n] * 1.0 / U[n, n]
        for i in range(n - 1, -1, -1):
            sum2 = 0
            for k in range(i + 1, n + 1):
                sum2 += U[i, k] * x[k]
            x[i] = (y[i] - sum2) * 1.0 / U[i][i] * 1.0
        return y, x