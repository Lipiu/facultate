import numpy as np

def populate():
    pop = []

    while len(pop) < 10:
        lista = np.random.uniform(-1, 1, 9).round(2).tolist()

        x10 = 1 - sum(lista)
        if -1 <= x10 <= 1:
            lista.append(round(x10, 2))
            pop.append(lista)
    return pop