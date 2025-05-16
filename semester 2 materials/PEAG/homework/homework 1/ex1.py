import numpy as np

def maxFunction():
    lista = []
    for i in range(30):
        while True:
            x = round(np.random.uniform(-2,7, 3))
            y = round(np.random.uniform(-2,7,3))
            z = round(np.random.uniform(-2,7,3))
            sum = x + y + z
            if(sum < 10):
                lista.append([x,y,z, round(x**2 - 2*y*z)])
                break
    return lista

print(maxFunction())