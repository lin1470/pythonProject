import numpy as np
from cumulate import cumulator

class trapezoid(cumulator):
    def cal(self,n):
        X = np.linspace(self.a,self.b,n+1)
        h = self.get_h(n)
        y = self.f(X)
        ans = np.sum(y[1:]) + np.sum(y[:-1])
        # f(a) + f(j) + f(b)
        return ans/2*h
