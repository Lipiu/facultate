import random

def solutie():
    try:
        n = int(input("N: "))
    except ValueError:
        print("ERROR! Please enter a valid integer.")
        return

    solutions = []

    for i in range(n):
        vector = [round(random.uniform(-1, 1), 4) for i in range(8)]
        sum_a = sum(vector[:4])
        sum_b = sum(vector[4:])
        if sum_a >= sum_b:
            quality = round(sum_a - sum_b, 4)
            vector.append(quality)
            solutions.append(vector)
    if solutions:
        max_quality = max(solution[-1] for solution in solutions)

        print("\nGenerated Individuals and their Quality:")
        for sol in solutions:
            print(sol)

        print("\nMaximum Quality:", max_quality)
    else:
        print("No valid solutions found based on the given condition.")

solutie()
