
import numpy as np

class cumulator:

    def __init__(self,a,b,f):
        self.a = a
        self.b = b
        self.f = f



    def get_h(self,n):
        return (self.b-self.a)/n

    def cal(self,n):
        return 0
