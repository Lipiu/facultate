import random


def populate():
    numberRows = int(input("N: "))
    solution = []
    i = 0

    while True:
        lista = []
        for j in range(8):
            lista.append(random.randint(0, 1))

        if sum(lista) % 2 == 1:
            i += 1
            nr = sum([lista[j] * 2 ** (7 - j) for j in range(8)])
            lista.append(nr)

            solution.append(lista)

        if i == numberRows:
            print("Generated individuals:")
            for individual in solution:
                print(individual[:-1])

            print("\nBest individuals with the highest quality:")
            max_q = max(individual[-1] for individual in solution)
            best_individuals = [individual[:-1] for individual in solution if individual[-1] == max_q]

            print(f"Max Quality: {max_q}")
            for individual in best_individuals:
                print(individual)
            return

populate()
