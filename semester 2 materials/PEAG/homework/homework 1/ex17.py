import random
import math

def solution():
    userInput = int(input("k= "))
    sol = []
    j = 0
    while True:
        lista=[]
        for i in range(userInput):
            lista.append(random.randint(1,6))


        if lista[-1]%2==0:
            lista.append(math.prod(lista))
            sol.append(lista)
            j = j + 1

        if j == 10:
            break
    for l in range (j):
        minEl = (min(elements[-1] for elements in sol))
        for element in sol:
            if element[-1] == minEl:
                print(element)
                sol.remove(element)
                break
solution()