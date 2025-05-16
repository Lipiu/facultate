import random


def generate_permutations(k):
    solutions = []

    for i in range(10):
        middle_part = list(range(2, k))
        random.shuffle(middle_part)

        permutation = [1] + middle_part + [k]

        quality = sum(1 for i in range(k) if permutation[i] < (i + 1))

        solutions.append(permutation + [quality])

    max_quality = max(sol[-1] for sol in solutions)

    print("\nGenerated Permutations (with quality values):")
    for sol in solutions:
        print(sol)

    print("\nMaximum Quality:", max_quality)


k = int(input("Enter value of k: "))
generate_permutations(k)
