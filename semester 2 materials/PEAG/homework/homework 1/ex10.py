import numpy as np

def populate():
    inputA = int(input("a: "))
    inputN = int(input("n: "))
    i = 0
    solution = []

    while True:
        lista = []
        for j in range(10):
            if np.random.randint(0,2) == 1:
                b = 1
            else:
                b = -1
            lista.append(b)
            np_lista = np.array(lista)

            if sum(np_lista) >= 0:
                solution.append(np_lista)
                i += 1
            if i == inputN:
                break
            print(solution)
            max_quality = max(sum(elements * inputA) for elements in solution)
            print("Max quality: " + str(max_quality))

populate()