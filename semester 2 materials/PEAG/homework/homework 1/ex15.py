import random

def generate_binary_vectors(n):
    solutions = []

    for _ in range(n):
        binary_vector = [0] * 9  # Initialize a 9-bit vector with all 0s

        ones_positions = random.sample(range(9), 5)
        for pos in ones_positions:
            binary_vector[pos] = 1

        quality = sum(ones_positions)

        binary_vector.append(quality)
        solutions.append(binary_vector)

    print("\nGenerated Individuals (Binary Vectors with Quality):")
    for sol in solutions:
        print(sol)

    return solutions

n = int(input("Enter the number of individuals (n): "))
generate_binary_vectors(n)
