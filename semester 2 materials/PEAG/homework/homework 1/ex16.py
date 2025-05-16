import random

def generate_permutations(n):
    solutions = []

    for _ in range(n):
        permutation = list(range(1, 8))
        random.shuffle(permutation)

        quality = sum(1 for i in range(6) if permutation[i] == i+2 and permutation[i+1] == i+1)

        permutation.append(quality)
        solutions.append(permutation)

    print("\nGenerated Permutations with Quality:")
    for sol in solutions:
        print(sol)

    max_quality = max(sol[-1] for sol in solutions)
    print("\nMaximum Quality:", max_quality)

n = int(input("Enter the number of permutations (n): "))
generate_permutations(n)
