import numpy as np

def generate_sorted_matrix():
    k = int(input("Enter the value of k: "))
    solutie = []
    for i in range(10):
        lista = [np.random.randint(0, 2) for i in range(k)]  # Generate individual
        quality = sum(1 for j in range(k - 1) if lista[j] == lista[j + 1])  # Compute quality
        lista.append(quality)
        solutie.append(lista)
    solutie.sort(key=lambda x: x[-1])  # Sort by quality
    for row in solutie:
        print(row)

generate_sorted_matrix()
