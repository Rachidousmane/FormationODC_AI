import random
import math
import numpy as np
import statistics as stat
L = list(())
x = 0
while x < 100:
    i = random.random()
    i = i*100 
    L.append(round(i, 2))
    x+=1

print("La liste est : ", L)
print("\nLa moyenne de la liste est : ", np.average(L))
print("\nLa variance de la liste est : ", np.var(L))
print("\nL'ecart type de la liste est : ", np.std(L))
print("\nLa mediane de la liste est : ", stat.median(L))