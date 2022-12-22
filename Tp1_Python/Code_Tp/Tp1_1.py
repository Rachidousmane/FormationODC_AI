from numpy import arctan
def funct1(x):
    return (x/(x**2+1))

def funct2(y):
    return arctan(y)

result = list()
sumR = float()
try:
    N = int(input("Donnez une valeur à N\n"))
except ValueError:
    print("Veuillez entrer un nombre entier")
else:
    L = list(range(-N, N+1, 1))
    sumR= sum([(funct1(i) - funct2(i))**2 for i in L])

    print("L = ", L)
    print("R = ", round(sumR, 2))
