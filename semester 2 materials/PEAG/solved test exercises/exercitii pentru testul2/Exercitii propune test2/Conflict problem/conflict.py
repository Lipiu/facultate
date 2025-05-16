# The N city-states of ancient Greece fight each other for domination, but when faced with a greater external
# threat they decide to unite. In order to establish a defense plan, delegates form all cities must meet. Each
# city will send only 1 ambassador. Knowing the historic rivalries between cities, use a genetic algorithm
# to find a way to seat the ambassadors around the negotiation table such that rival cities ambassadors are
# not next to each other (assuming this is possible).
# The map of rivalries is described through a square matrix of size N, called CONFLICT:
# 𝐶𝑂𝑁𝐹𝐿𝐼𝐶𝑇(𝑖,𝑗) = {
# 0, 𝑖𝑓 𝑐𝑖𝑡𝑖𝑒𝑠 𝑖 𝑎𝑛𝑑 𝑗 𝑎𝑟𝑒 𝑛𝑜𝑡 𝑖𝑛 𝑐𝑜𝑛𝑓𝑙𝑖𝑐𝑡

#starting the solution
import numpy as np

# ---------------------------- Fitness Function ----------------------------
def fitness(individual, conflictMatrix):
    numCities = len(individual)
    penalty = 0
    for i in range(numCities):
        city1 = individual[i]
        city2 = individual[(i + 1) % numCities]  # round table wrap-around
        if conflictMatrix[city1][city2] == 1:
            penalty += 1
    return -penalty  # Fewer penalties = better fitness

# ---------------------------- Population Generation ----------------------------
def generatePopulation(populationSize, numCities):
    population = []
    for _ in range(populationSize):
        individual = np.random.permutation(numCities).tolist()
        population.append(individual)
    return population

# ---------------------------- Probability Calculation ----------------------------
def calculateProbability(population, conflictMatrix):
    fitness_values = [fitness(ind, conflictMatrix) for ind in population]
    min_fitness = min(fitness_values)
    shifted_fitness = [f - min_fitness + 1 for f in fitness_values]  # make all positive
    total = sum(shifted_fitness)
    probabilities = [f / total for f in shifted_fitness]
    return probabilities

# ---------------------------- Roulette Wheel Selection ----------------------------
def rouletteSelection(population, conflictMatrix):
    probabilities = calculateProbability(population, conflictMatrix)
    selected_indices = np.random.choice(len(population), size=len(population), p=probabilities)
    return [population[i] for i in selected_indices]

# ---------------------------- Permutation-Safe Crossover ----------------------------
def crossover(parent1, parent2):
    size = len(parent1)
    child = [-1] * size
    start, end = sorted(np.random.choice(range(size), 2, replace=False))

    # Copy segment from parent1
    child[start:end] = parent1[start:end]

    # Fill in from parent2 in order
    fill_pos = end
    for city in parent2:
        if city not in child:
            if fill_pos >= size:
                fill_pos = 0
            child[fill_pos] = city
            fill_pos += 1
    return child

# ---------------------------- Offspring Generation ----------------------------
def generateOffspring(selectedIndividuals):
    offspring = []
    for i in range(0, len(selectedIndividuals), 2):
        parent1 = selectedIndividuals[i]
        parent2 = selectedIndividuals[(i + 1) % len(selectedIndividuals)]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        offspring.append(child1)
        offspring.append(child2)
    return offspring

# ---------------------------- Mutation ----------------------------
def mutate(individual, mutation_rate):
    if np.random.random() < mutation_rate:
        pos1, pos2 = np.random.choice(len(individual), 2, replace=False)
        individual[pos1], individual[pos2] = individual[pos2], individual[pos1]
    return individual

def applyMutation(offspring, mutationRate):
    return [mutate(ind, mutationRate) for ind in offspring]

# ---------------------------- Genetic Algorithm Runner ----------------------------
def runGA(conflictMatrix, population_size=10, mutation_rate=0.1, generations=50):
    num_cities = len(conflictMatrix)
    population = generatePopulation(population_size, num_cities)

    for generation in range(generations):
        print(f"Generation {generation + 1}")

        # Evaluate fitness of each individual
        fitness_scores = [fitness(ind, conflictMatrix) for ind in population]
        best_fitness = max(fitness_scores)
        best_individual = population[fitness_scores.index(best_fitness)]
        print(f"  Best fitness: {-best_fitness} conflicts")
        print(f"  Best arrangement: {best_individual}")

        # Stop early if solution has no conflicts
        if -best_fitness == 0:
            print("✅ Conflict-free seating found!")
            break

        # Generate next generation
        selected = rouletteSelection(population, conflictMatrix)
        offspring = generateOffspring(selected)
        population = applyMutation(offspring, mutation_rate)

# ---------------------------- Example Usage ----------------------------
if __name__ == "__main__":
    # Example conflict matrix of 4 cities
    conflictMatrix = np.array([
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ])

    runGA(conflictMatrix, population_size=10, mutation_rate=0.2, generations=100)

