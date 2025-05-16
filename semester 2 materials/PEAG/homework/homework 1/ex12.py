import random
import numpy as np


def solution():
    solutie=[]

    for j in range(10):
        lista=[]
        quality=0
        for i in range(7):
            lista.append(random.randint(0,1))
            if lista[i]==1 and (i+1)%2==1:
                quality=quality+1
        lista.append(quality)
        solutie.append(lista)

    print (solutie)
    suma=0
    for elements in solutie:
        suma=elements[-1]+suma
    avg=suma/10
    print("Average quality:",avg)

solution()