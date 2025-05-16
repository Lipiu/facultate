import random

def solution():
    userInput = int(input("n: "))
    i = 0
    lista = []

    while True:
        x = random.uniform(-2 ,2)
        y = random.uniform(-2, 2)
        z = random.uniform(-2, 2)

        total = x + y + z

        if total >= -2 and total <= 2:
            solution.append([x, y, z, total])
            i = i + 1
        if i == userInput:
            break
    print(solution)