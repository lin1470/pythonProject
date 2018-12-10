from trapezoid import trapezoid
from cumulate import cumulator
import numpy as np
class extrapolate(cumulator):

    def __init__(self,a,b,f):
        cumulator.__init__(self,a,b,f)
        self.caculater = trapezoid(a,b,f)

    def degree_cal(self,n,degree):
        if degree == 0:
            return self.caculater.cal(n)

        return (self.degree_cal(2*n,degree-1)*(4**degree) - self.degree_cal(n,degree-1))/(4**degree-1)

