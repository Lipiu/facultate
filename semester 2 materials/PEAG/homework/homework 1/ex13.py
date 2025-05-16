import numpy as np

def maximize_function():
    a = np.array([int(input(f"a[{i}]: ")) for i in range(7)])

    solutions = []
    evaluations = []

    for i in range(10):
        while True:
            x = np.round(np.random.uniform(-10, 10, 7), 2)
            if np.sum(x) <= 10:
                solutions.append(x)
                evaluations.append(np.dot(a, x))
                break

    max_value = max(evaluations)
    max_solution = solutions[evaluations.index(max_value)]

    print("Generated Solutions:")
    for sol in solutions:
        print(sol)

    print("\nMaximum Quality:", max_value)
    print("Best Solution:", max_solution)

maximize_function()
