from math import *

def combinaciones(x, y):
    return factorial(x) / float(factorial(y)*factorial(x-y))

def probabilidad(p, i):
    n_max = floor((p-i)/float(6))+1
    acc = 0
    for n in range(n_max):
        val1 = (-1)**n;
        val2 = combinaciones(i, n)
        val3 = combinaciones(p-(6*n)-1, i-1)
        acc += (val1 * val2 * val3)
    return acc / float(6**i)

n = float(input("Ingrese la cantidad de dados\n"))

s = float(input("Ingrese la suma cuya probabilidad desea saber\n"))

print ("El porcentaje de probabilidad es")
print(str((probabilidad(s,n))*100))