from math import *

def combinaciones(x, y):
    return factorial(x) / float(factorial(y)*factorial(x-y))

def probabilidad(p, i):
    sup = floor((p-i)/float(6))+1
    a = 0
    for n in range(sup):
        x1 = (-1)**n;
        x2 = combinaciones(i, n)
        x3 = combinaciones(p-(6*n)-1, i-1)
        a += (x1 * x2 * x3)
    return a / float(6**i)

n = float(input("Ingrese la cantidad de dados\n"))


s = float(input("Ingrese la suma cuya probabilidad desea saber\n"))


print ("El porcentaje de probabilidad es")
print(str((probabilidad(s,n))*100))
