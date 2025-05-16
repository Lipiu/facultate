# A product P is produced in 2 factories (București and Craiova) and is stored for distribution in 3
# warehouses (Ploiești, Pitești and Cluj). The factory in București can produce 120 tons per week and the
# factory in Craiova can produce 140 tons per week. The warehouses need the following quantities each
# week: 
#       Ploiești needs 100 tons, 
#       Pitești needs 60 tons and 
#       Cluj needs 80 tons. 
#The table below shows the transport cost for 1 ton from factories to warehouses.
# Transport cost for 1 ton Ploiești Pitești Cluj
# București 50 70 90
# Craiova 60 70 100
# Use a genetic algorithm to find how many tons of each product should be supplied from each factory to
# each warehouse to minimize the transport cost. 

import random
import numpy as np

#constants
production = [120, 140] #tons
quantities = [100, 60, 80] #tons
cost_per_ton_buc = [50, 70, 90]
cost_per_ton_craiova = [60, 70, 100]

# 2 factories: Bucuresti, Craiova
# 3 warehouses: Ploiesti, Pitesti, Cluj

def generate_chromosome():
    # Bucuresti - max 120 tons
    b1 = random.randint(0, 120) # Bucuresti - Ploiesti
    b2 = random.randint(0, 120 - b1) # Bucuresti - Pitesti
    b3 = random.randint(0, 120 - b1 - b2) # Bucuresti - Cluj

    # Craiova - max 140 tons
    c1 = random.randint(0, 140) # Craiova - Ploiesti
    c2 = random.randint(0, 140 - c1) # Craiova - Pitesti
    c3 = random.randint(0, 140 - c1 - c2) # Craiova - Cluj

    return [b1,b2,b3,c1,c2,c3]

def fitness(chromosome):
    BP, BPi, BC, CP, CPi, CC = chromosome
    cost = (
        BP * cost_per_ton_buc[0] + BPi * cost_per_ton_buc[1] + BC * cost_per_ton_buc[2] +
        CP * cost_per_ton_craiova[0] + CPi * cost_per_ton_craiova[1] + CC * cost_per_ton_craiova[2]
    )

    penalty = 1000
    demands = quantities
    delivered = [
        BP + CP, # Ploiesti total delivery
        BPi + CPi, # Pitesti total delivery
        BC + CC # Cluj total deliverry
    ]

    total_penalty = 0
    for i in range(len(demands)):
        total_penalty += abs(delivered[i] - demands[i]) * penalty

    return cost + total_penalty

def initialize_pop(pop_size):
    population = []
    for _ in range(pop_size):
        chromosome = generate_chromosome()
        population.append(chromosome)
    return population

def evaluate_pop(population):
    fitness_value = []
    for chromosome in population:
        fitness_score = fitness(chromosome)
        fitness_value.append(fitness_score)
    return fitness_value

def tournament_selection(population, fitness_values, tournament_size=3):
    selected_parents = []
    pop_size = len(population)
    for _ in range(2):
        competitors_idx = random.sample(range(pop_size), tournament_size)
        best_idx = min(competitors_idx, key=lambda i: fitness_values[i])
        selected_parents.append(population[best_idx])
    return selected_parents[0], selected_parents[1]

def single_point_crossover(parent1, parent2):
    length = len(parent1)
    crossover_point = random.randint(1, length - 1)

    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]

    return child1, child2

def mutate(chromosome, mutation_rate=0.7):
    mutated = chromosome.copy()
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            change = random.randint(-10,10)
            mutated[i] = max(0, mutated[i] + change)
    return mutated

def genetic_algorithm(pop_size, generations, mutation_rate):
    population = initialize_pop(pop_size)

    for gen in range(generations):
        fitness_value = evaluate_pop(population)

        new_population = []

        while(len(new_population) < pop_size):
            # Selection
            parent1, parent2 = tournament_selection(population, fitness_value)

            #Crossover
            child1, child2 = single_point_crossover(parent1, parent2)

            # Mutation
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)

            new_population.extend([child1,child2])
        
        population = new_population[:pop_size]

        best_fitness = min(fitness_value)
        print(f"Generation {gen + 1} - Best fitness: {best_fitness}")
    
    fitness_value = evaluate_pop(population)
    best_index = fitness_value.index(min(fitness_value))
    best_solution = population[best_index]

    return best_solution

if __name__ == "__main__":
    best = genetic_algorithm(50, 100, 0.7)
    print("Best solution: ", best)
    print("Best fitness: ", fitness(best))