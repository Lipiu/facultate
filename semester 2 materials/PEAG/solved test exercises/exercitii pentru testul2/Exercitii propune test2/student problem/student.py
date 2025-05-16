# At the beginning of the university year a student must chose some courses. The available budget is 10000
# units and three types of courses are available:
# a. Cost: 1000 units, credit points: 5, individual study required: 80 hours;
# b. Cost: 800 units, credit points: 3, individual study hours required: 40 hours;
# c. Cost: 1500 units, credit points: 8, individual study hours required: 100 hours.
# Use a genetic algorithm to help the student choose a combination of course (how many of each type) such
# that it fits within the available budget, maximizes the average number of credits and the average individual
# study hours is at most 70.
# Note: average number of credits per course and average number of study hours per course are computed
# as weighted average.

import numpy as np
import random

# Constants
BUDGET = 10000 #rich af
costs = [1000, 800, 1500]
credit_points = [5,3,8]
individual_study_hours_required = [80,40,100]

# Constraints
# 1. fit withing budget of 10000
# 2. maximize the average number of credits
# 3. average individual study hours <= 70

def total_cost(a,b,c):
    return costs[0] * a + costs[1] * b + costs[2] * c

def calculate_average_credit_points(a,b,c):
    #weighted average: (sum(cost * credit_points)) / sum(cost) -> sum adica suma d aia E de la mate fram
    total_courses = a + b + c
    if total_courses == 0:
        return 0
    total_credits = a * credit_points[0] + b * credit_points[1] + c * credit_points[2]
    return total_credits / total_courses

def calculate_average_study_hours(a,b,c):
    #weighted average:
    total_courses = a + b + c 
    if total_courses == 0:
        return 0
    total_study_hours = a * individual_study_hours_required[0] + b * individual_study_hours_required[1] + c * individual_study_hours_required[2]
    return total_study_hours / total_courses

def generate_population(size):
    population = []
    attempts = 0
    max_attempts = size * 100

    while len(population) < size and attempts < max_attempts:
        a = random.randint(0, BUDGET // costs[0])
        b = random.randint(0, BUDGET // costs[1])
        c = random.randint(0, BUDGET // costs[2])

        #check constraints
        if(total_cost(a,b,c) <= BUDGET):
            population.append((a,b,c))
        attempts += 1
        
    if len(population) < size:
        raise ValueError(f"Could only generate {len(population)} valid individuals; needed {size}.")
    return population


def fitness(individual):
    a,b,c = individual
    cost = total_cost(a,b,c)
    avg_credit_points = calculate_average_credit_points(a,b,c)
    avg_study_hours = calculate_average_study_hours(a,b,c)

    penalty = 0

    if cost > BUDGET:
        penalty += (cost - BUDGET) * 0.1
    if avg_study_hours > 70:
        penalty += (avg_study_hours - 70) * 2
    if (a + b + c) == 0:
        penalty += 10
    
    return avg_credit_points - penalty

def tournament_selection(population):
    selected = random.sample(population, 3)
    selected = sorted(selected, key=fitness, reverse=True)
    return selected[0]

def crossover(parent1, parent2):
    child = (
        random.choice([parent1[0], parent2[0]]),
        random.choice([parent1[1], parent2[1]]),
        random.choice([parent1[2], parent2[2]])
    )
    if total_cost(*child) <= BUDGET:
        return child
    else:
        return parent1

def mutate(individual, mutation_rate=0.7):
    a, b, c = individual
    if random.random() < mutation_rate:
        a = max(0, a + random.choice([-1, 1]))
    if random.random() < mutation_rate:
        b = max(0, b + random.choice([-1, 1]))
    if random.random() < mutation_rate:
        c = max(0, c + random.choice([-1, 1]))

    if total_cost(a,b,c) > BUDGET:
        return individual
    return (a,b,c)

def genetic_algorithm(pop_size, generations):
    population = generate_population(pop_size)
    print(f"Initial population: {len(population)}")
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

        # elitism
        best_individual = max(population, key=fitness)
        replace_index = random.randint(0, pop_size - 1)
        new_population[replace_index] = best_individual

        print(f"Gen {gen}: Best fitness: {fitness(best_individual):.2f}")

        population = new_population

    best_individual = max(population, key=fitness)
    return best_individual, fitness(best_individual)


if __name__ == "__main__":
    best_solution, best_fit = genetic_algorithm(50, 50)
    print("Best solution found: ", best_solution)
    print("Total cost: ", total_cost(*best_solution))
    print("Average number of credits: ", calculate_average_credit_points(*best_solution))
    print("Average number of study hours: ", calculate_average_study_hours(*best_solution))