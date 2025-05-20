## Problema magazin cu fructe (problema 7)
### Cerinta
 A factory packs dehydrated fruits to be sold in stores. The raw materials used are: figs, pineapple, dates,
cranberry. The available quantities of each raw material are, in order: 100, 80, 120, 50 kg. The factory
packs the following combinations, in 200g packs:
- Combination 1: 30% figs, 25% pineapple, 25% dates, 20% cranberries;
- Combination 2: 75% dates, 25% figs;
- Combination 3: 25% figs, 25% pineapple, 25% dates, 25% cranberries;
- Combination 4: 100% dates;
- Combination 5: 100% figs.

The profits brought by each type of pack are, in order: 20, 10, 15, 12, 5 units per pack.
Use a genetic algorithm to decide how many packs of each type should be produced to maximize the
profit. 

##
**1.** `Inputs`
* DIM = dimension of the population
* N = number of raw materials
    * raw materials available:
        * figs = 100 kg
        * pineapple = 80 kg
        * dates = 120 kg
        * cranberries = 50 kg
* M = number of generations
* Vectors
    * Raw materials available
    * Combinations
        * [0.3, 0.25, 0.25, 0.2] -> figs, pineapple, dates, cranberries
        * [0.75, 0.25] -> dates, figs
        * [0.25, 0.25, 0.25, 0.25] -> figs, pineapple, dates, cranberries
        * [1] -> dates
        * [1] -> figs
    * Profits
        * in order: 20, 10, 15, 12, 5
##
**2.** `Representation`
* Vector of integers [x1, x2, x3, x4, x5]
* Problem with constraints
    * Cannot exceed available raw materials
##
**3.** `Solution space`
* Exponential for integer representation
##
**4.** `Fitness`
* x: genotype = [x1, x2, x3, x4, x5] where xi = number of packs of combination i
* total_profit(x) = 20·x1 + 10·x2 + 15·x3 + 12·x4 + 5·x5

* A genotype is feasible if for each fruit type, the total amount used across all xi does not exceed availability.

* Goal: maximize the profit
* A feasible genotype respects the constraint
##
**5.** `Population model`
* Constant size over time
* Generational model with constraints
##
**6.** `Generation of initial population`
* Random with verification of feasibility and evaluation
* Unfeasible individuals are discarded and new ones are generated
##
**7.** `Parent selection`
* Generational model
* From `dim` candidates select `dim` parents
* We can use SUS mechanism with FPS without sigma scaling because fitness can be negative
##
**8.** `Crossover`
* On population level
* General crossover scheme for problems with constraints
* Crossover probability pc > 0.5 (usually 0.7 or 0.8)
* Any unfeasible individual is replaced with a clone of a parent
* For each pair of parents
    * Multiple crossover operator
* Representation is vector of integers
* Use uniform or arithmetic crossover for integer vectors.
* Use uniform integer mutation

##
**9.** `Mutation`
* On population level
* General mutation scheme for problems with constraints
* Any unfeasible individual is discarded and the mutation is cancelled for that individual
* Probability of mutation pm is usually very low (0.1)
* Mutation operator for permutation
##
**10.** `Select next generation`
* Since we use a generational model we use `elitism`
##
**11.** `Stop condition`
* We reach the limited number of steps
* If fitness is the same for all generations
* When optimum value is reached
* If over the last k generations (given parameter) the fitness hasn't changed