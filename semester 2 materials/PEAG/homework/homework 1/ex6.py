import random

def populate(n):
    max_quality = -1
    best_permutation = None
    solution = []

    for i in range(n):
        perm = list(range(8))
        random.shuffle(perm)
        quality = 0
        for i in range(len(perm)):
            for j in range(i + 1, len(perm)):
                if(perm[i] == j and perm[j] == 1):
                    quality += 1
        solution.append((perm,quality))

        if quality > max_quality:
            max_quality = quality
            best_permutation = perm
    print(f"Generated Permutations and their Quality:")
    for perm, quality in solution:
        print(f"Permutation: {perm}, Quality: {quality}")

    print(f"\nMaximum Quality: {max_quality}")
    best_permutations = [perm for perm, quality in solution if quality == max_quality]
    print(f"Best Permutations with Maximum Quality:")
    for perm in best_permutations:
        print(perm)

n = int(input("N:"))
populate(n)


