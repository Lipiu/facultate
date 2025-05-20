## Air transportation problem (problem 2)

**1.** `Inputs`
* Dim: Population size
* N: number of planes types
* M: number of generations
* Vectors:
    * x = [a,b,c] number of planes of each type
    * Type a
        * Cost = 100 units
        * Autonomy = 6000 km
        * TCAS = 30 km
    
    * Type b
        * Cost = 60 units
        * Autonomy = 4200 km 
        * TCAS = 48 km
    
    * Typce c
        * Cost = 50 units
        * Autonomy = 2800 km
        * TCAS = 32 km
* Budget: 5000 units
##
**2.** `Representation`
* Type: Vector of integers
* Each vector element:
    * x[0] = a --> number of planes of type a
    * x[1] = b --> number of planes of type b
    * x[2] = c --> number of planes of type c
##
**3.** `Constraints`
* Problem with constraints
    * Total cost <= 5000
    * Average TCAS detection range >= 40
##
**4.** `Solution space`
* Solution space is **exponential** due to combinations of intege vectors under constraint
##
**5.** `Fitness`
* x (genotype): Vector[a,b,c]
* Total cost = 100a + 60b + 50c
* Average autonomy: $$
                    \frac{6000a + 4200b + 2800c}{a + b + c}
                   $$
* Average TCAS:$$
                    \frac{30a + 48b + 32c}{a + b + c}
                   $$

* Goal: Maximize average autonomy
* A feasible genotype must satisfy all constraints
##
**5.** `Population model`
* Model: Generational with constraints
* Population size constant over time
##
**6.** `Generation of initial population`
* Randomly generate [a,b,c] where:
    * Each value is an integer >= 0
    * Total cost <= 5000
    * avg TCAS >= 40

* Feasibility check
    * if constraints are not met discard the individual and generate a new one
* Evaluate fitness only for feasible solutions
##
**7.** `Parent selection`
* Model: generational
* Select `dim` parents from the current population
* Use Stochastic Universal Sampling (SUS)
* Use FPS `without` sigma scaling (since fitness can be negative only for infeasible ones, which are already discarded)
##
**8.** `Crossover`
* Population level
    * General crossover for integer vector problems with constraints
    * Use crossover probability pc = 0.8
    * If a child is unfeasible --> replace with parent clone

* For each parent pair
    * Use uniform crossover for integer vectors
    * Or arithmetic crossover with rounding to integer
##
**9.** `Mutation`
* Population level:
    * Apply mutation with feasiblity check
    * Probability pm = 0.1
    * If mutation results in an unfeasible individual --> discard the mutation

* Mutation operator
    * For integer vector: apply uniform mutation (add or subtract small random integer)
    * Example: increase or decrease a, b, or c by ±1, within bounds
##
**10.** `Selection of next generation`
* Use elitism
    * Carry over the best individual from current generation
    * Fill the rest with offspring from crossover/mutation
##
**11.** `Stop condition`
* Maximum number of generations reached (M)
* Best fitness value remains constant for the last k generations
* No further improvement possible
