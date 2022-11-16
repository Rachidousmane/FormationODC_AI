import random

class DataTrans:
    def __init__(self, n, s):
        self.n = n
        self.s = s
    
    def G(self):
        K = list()
        x = 0
        while x < self.s:
            i = random.random()
            y = i*100
            K.append(round(y,2))
            x+=1
        return K
    def MIN(self, z):
        lmini = z[0]
        for i in range(len(z)):
            if z[i] < lmini:
                lmini = z[i]
        return lmini
    def MAX(self, z):
        lmaxi = z[0]
        for i in range(len(z)):
            if z[i] > lmaxi:
                lmaxi = z[i]
        return lmaxi
    def funct(self, x):
        t = pow(x,3) + 3*(pow(x,2)) - 5
        return round(t,2)
    def image(cls, X):
        T = list()
        for i in range(len(X)): 
            T.append(cls.funct(X[i]))
        return T