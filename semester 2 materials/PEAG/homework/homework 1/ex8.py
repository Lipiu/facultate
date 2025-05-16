import random


def generate_matrix_and_find_weakest(k):
    matrix = []
    for i in range(10):
        while True:
            individual = [random.choice([-4, -3, -2, -1, 1, 2, 3, 4]) for i in range(k)]
            if sum(individual) > 0:
                break

        quality = sum(abs(x) for x in individual)
        matrix.append((individual, quality))

    min_quality = min(quality for i, quality in matrix)
    weakest_individuals = [individual for individual, quality in matrix if quality == min_quality]
    print("Generated Matrix (Individual, Quality):")
    for individual, quality in matrix:
        print(f"Individual: {individual}, Quality: {quality}")

    print("\nWeakest Individuals (Minimum Quality):")
    for individual in weakest_individuals:
        print(f"Individual: {individual}, Quality: {min_quality}")



generate_matrix_and_find_weakest(3)
