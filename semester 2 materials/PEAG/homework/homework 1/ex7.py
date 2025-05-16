import numpy as np
import random

def populate():
    n = int(input("Number of rows: "))
    solutie = []
    for i in range(n):
        lista=[]
        for j in range(8):
            if j!=4:
                lista.append(random.randint(1,4))
            else:
                lista.append(random.randrange(1,3,2))
        lista.append(int(np.prod(lista)))
        solutie.append(lista)
    print(solutie)

    min_quality = min(elements[-1] for elements in solutie)
    print("Minimum quality: ", min_quality)
    print("Weakest individuals: ")
    for i in range(n):
        if solutie[i][-1] == min_quality:
            print(solutie[i])

populate()