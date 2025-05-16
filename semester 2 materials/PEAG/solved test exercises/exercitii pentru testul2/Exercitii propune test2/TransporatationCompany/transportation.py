# An air transportation company wants to buy 3 types of planes, with an acquisition budget of 5000 units.
# Each type of plane has the following features of interest:
# a. Cost: 100 units, autonomy: 6000km, TCAS detection range: 30km.
# b. Cost: 60 units, autonomy: 4200km, TCAS detection range: 48km.
# c. Cost: 50 units, autonomy: 2800km, TCAS detection range: 32 km.
# Determine how many aircrafts of each type should be bought such that
# o Total cost is not above budget,
# o Average autonomy is maximized,
# o Average TCAS detection range is at least 40 km.
# Notes:
# 1. if the number of planes bought from each type is denoted as a, b and c, then the average
# autonomy is 6000∙𝑎 + 4200∙𝑏 + 2800∙𝑐
# 𝑎+𝑏+𝑐
# average TCAS detection range is 30∙𝑎+48∙𝑏+32∙𝑐
# 𝑎+𝑏+𝑐
#2. The problem can be
# solved in two versions: consider only the restriction above, or consider an additional restriction that
# requires to spend the budget (do not leave unspent money, if they are enough to buy more planes)

import numpy as np
import random

import random

# Constants
BUDGET = 5000
prices = [100, 60, 50]
autonomy = [6000, 4200, 2800]
TCAS = [30, 48, 32]


def total_cost(a, b, c):
    return prices[0] * a + prices[1] * b + prices[2] * c


def calculate_average_autonomy(a, b, c):
    total_planes = a + b + c
    if total_planes == 0:
        return 0
    return (autonomy[0] * a + autonomy[1] * b + autonomy[2] * c) / total_planes


def calculate_average_TCAS(a, b, c):
    total_planes = a + b + c
    if total_planes == 0:
        return 0
    return (TCAS[0] * a + TCAS[1] * b + TCAS[2] * c) / total_planes


def generate_individual():
    while True:
        a = random.randint(0, BUDGET // prices[0])
        b = random.randint(0, BUDGET // prices[1])
        c = random.randint(0, BUDGET // prices[2])
        if total_cost(a, b, c) <= BUDGET:
            return (a, b, c)


def initialize_population(size):
    return [generate_individual() for _ in range(size)]


def fitness(individual):
    a, b, c = individual
    cost = total_cost(a, b, c)
    avg_tcas = calculate_average_TCAS(a, b, c)
    avg_autonomy = calculate_average_autonomy(a, b, c)

    penalty = 0
    if cost > BUDGET:
        penalty += 1000 * (cost - BUDGET)  # heavy penalty
    if avg_tcas < 40:
        penalty += 1000 * (40 - avg_tcas)
    if a + b + c == 0:
        penalty += 1000  # avoid empty solutions

    return avg_autonomy - penalty


def tournament_selection(population, k=3):
    selected = random.sample(population, k)
    selected = sorted(selected, key=fitness, reverse=True)
    return selected[0]


def crossover(parent1, parent2):
    child = (
        random.choice([parent1[0], parent2[0]]),
        random.choice([parent1[1], parent2[1]]),
        random.choice([parent1[2], parent2[2]]),
    )
    if total_cost(*child) <= BUDGET:
        return child
    else:
        return parent1  # fallback


def mutate(individual, mutation_rate=0.1):
    a, b, c = individual
    if random.random() < mutation_rate:
        a = max(0, a + random.choice([-1, 1]))
    if random.random() < mutation_rate:
        b = max(0, b + random.choice([-1, 1]))
    if random.random() < mutation_rate:
        c = max(0, c + random.choice([-1, 1]))

    if total_cost(a, b, c) > BUDGET:
        return individual  # discard mutation if invalid
    return (a, b, c)


def genetic_algorithm(pop_size=100, generations=100):
    population = initialize_population(pop_size)

    for gen in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])
        population = new_population

        # Optional: print best fitness
        best = max(population, key=fitness)
        print(f"Gen {gen}: Best fitness = {fitness(best):.2f} Planes: {best}")

    best = max(population, key=fitness)
    return best, fitness(best)


if __name__ == "__main__":
    best_solution, best_fit = genetic_algorithm()
    print("Best solution found:", best_solution)
    print("Fitness (average autonomy):", best_fit)
    print("Total cost:", total_cost(*best_solution))
    print("Average TCAS:", calculate_average_TCAS(*best_solution))
