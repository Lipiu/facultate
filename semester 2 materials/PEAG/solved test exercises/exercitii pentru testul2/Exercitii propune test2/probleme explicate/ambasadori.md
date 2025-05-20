## Ambassador problem (problem 1)

**1.** `Inputs`
* DIM = dimension of the population
* N = number of cities (number of ambassadors)
* M = number of generations

* Vectors: 
    * CONFLICT MATRIX: a symmetric NxN matrix where:
        * CONFLICT(i,j) = 1 if city i and city j are enemies
        * CONFLICT(i,j) = 0 if city i and city j are NOT enemies
##
**2.** `Representation`
* Type: permutation of integers

* Each vector element: an integer from 0 to N-1, representing one city

* Vector meaning: the order in which the ambassadors are seated at the round table
##
**3.** `Constraints`
* **Hard constraint**: no two rival cities ambassadors (as per conflict matrix) can stand next to each other
##
**4.** `Representation in solution space`
* Each solution is a permutation of the cities representing a circular seating order

* Example: N = 6 --> [1, 2, 3, 4, 5, 6]
    * seat city 1 at the table
    * seat city 2 next to city 1
    * seat city 3 next to city 2
    * seat city 4 next to city 3
    * seat city 5 next to city 4
    * seat city 6 next to city 5
    * seat city 6 next to city 1 (circular table)
##
**5.** `Solution space`
* All possible permutations of N cities

* Size = N! (factorial), so the space is discrete, finite and large as N grows
##
**6.** `Fitness function`
* x (genotype): a permutation vector representing a seating arrangement
* Description:
    * Evaluate the number of adjacent rival pairs around the table using the CONFLICT matrix
    * Since seating is circular, neighbours include the last and the first ambassador
* Goal:
    * The goal is to minimize the number of conflicts
    * if fitness = 0 that means the perfect fitness (0 conflicts)

* A feasible genotype has f(x) = 0 which means 0 conflicts (no adjacent rivals)
##
**7.** `Population model (with constant size)`
* Model: Generational model with constraints
* Population size stays constant over time
##
**8.** `Generation of initial population`
* Random generation of permutations
* For each individual
    * Check if it is feasible (no rival pairs adjacent)
    * if unfeasible, discard and generate new one

* Evaluate each feasible individual using fitness function
##
**9.** `Parent selection`
* Model: generational selection
* From the current population select `dim` parents
* Selection mechanism
    * We can use Stochastic Universal Sampling (SUS)
    * We can use Fitness Proportional Selection (FPS) **without** sigma scalling, since fitness can be negative
##
**10.** `Crossover`
* Population level:
    * Use a general crossover scheme with constraints.

* Crossover probability
    * pc > 0.5
​
* If a child is unfeasible, replace it with a clone of one parent.
* For each pair of parents:
    * Representation type: permutation.
    * Problem type: adjacency-dependent.
    * Use Partially Mapped Crossover (PMX).
##
**11.** `Mutation`
* Population level:
    * Apply mutation with constraint checking.

    * Mutation probability: pm = 0.1 (low)
    * If a mutated individual is unfeasible, discard it (cancel mutation).

* Mutation operator:
    * Type: permutation
    * Use swap mutation: randomly pick two indices and swap them.
##
**12.** `Selection of Next Generation`
* Strategy: Elitism.
    * Carry forward the best individual(s) unchanged.
    * Fill the rest of the population with new offspring.
##
**13.** `Stop Condition`
* Stop the algorithm if one of the following is true:
    * A maximum number of generations (M) is reached.
    * The fitness is the same for all individuals.
    * An optimal solution (fitness = 0) is found.
    *Over the last k generations (a defined threshold), the best fitness has not changed.