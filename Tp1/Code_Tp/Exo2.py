import random

#question 1
D = list(())
print("Donner le nombre liste : ")
N = int(input())
print("Donner une taille chaque liste : ")
n = int(input())
def G():
    K = list()
    x = 0
    while x < n:
        i = random.random()
        y = i*100 
        K.append(round(y,2))
        x+=1
    return K
i = 0
while i < N:
    D.append(G())
    i += 1
print("La liste est D : ", D)

#Question 2
def MIN(z):
    lmini = z[0]
    for i in range(len(z)):
        if z[i] < lmini:
            lmini = z[i]
    return lmini
def MAX(z):
    lmaxi = z[0]
    for i in range(len(z)):
        if z[i] > lmaxi:
            lmaxi = z[i]
    return lmaxi
L = list()
p = 0
while p<N:
    print("\nLe Min de la", p ,"ième liste est", MIN(D[p]))
    L.append(MIN(D[p]))
    p+=1
u = 0
while u<N:
    print("\nLe Max de la", u ,"ième liste est", MAX(D[u]))
    L.append(MAX(D[u]))
    u+=1
print("\nLe Min global de la liste D est", MIN(L))
print("\nLe Max global de la liste D est", MAX(L))

def f(X, i):
    t = pow(X[i],3) + 3*(pow(X[i],2)) - 5
    return t

def image(X):
    T = list(())
    for i in range(len(X)):
        T.append(round(f(X, i), 2))
    return T


D1 = list()
u = 0
while u<N:
    D1.append(image(D[u]))
    u+=1
    
print("\nla liste D1 est : ",D1)