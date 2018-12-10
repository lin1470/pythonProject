import numpy as np
from cumulate import cumulator


class simpthon(cumulator):
    def cal(self, n):
        X = np.linspace(self.a,self.b,2*n+1)
        h = self.get_h(n)
        y = self.f(X)
        ans = 0

        for i in range(0, n*2, 2):
            ans += y[i] + y[i+2] + 4*y[i+1]

        return ans*h/6


