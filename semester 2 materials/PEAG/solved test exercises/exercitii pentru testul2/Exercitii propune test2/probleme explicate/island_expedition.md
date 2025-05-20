## Visiting islands problem (problem 8)
**Cerinta problema**\
A university organizes a scientific expedition by sea to visit some virgin islands in X archipelago, starting
from one port of the archipelago and returning to the same port. The ship cannot be supplied during
voyage. The available resources on board allow visits to only n islands from 1000 islands that form the
archipelago n<<1000) and a total travel distance of k km. use a genetic algorithm to choose the islands
to be visited and the order to visit them. It is preferred to visit islands as far away as possible. The
distances between islands (including the home port) are given as a weight matrix in a text file, where
D(i,j) = distance between islands i and j.
##

**1.** `Inputs`
* DIM = dimension of the population
* N = number of islands
* M = number of generations
* Vectors
    * D[i][j] = distance between islands i and j
    * k = total travel distance (km)
    * n = number of distinct islands to select and visit
##
**2.** `Representation`
* Type: permutations
* It is a problem with constraints
    * The ship cannot be supplied during the voyage
    * `n << 1000` --> available resources allow visits to only n islands from 1000
    * total travel distance of `k` km
##
**3.** `Solution space`
* Solution space for this problem is exponential
##
**4.** `Fitness`
* x: genotype --> a permutation of `n` unique islands
* Goal: Visit as many islands as possible, maximizing the distance traveled (preferred long distanced islands)
* A feasible genotype respects all constraints
##
**5.** `Population model`
* Generational model with constraints
##
**6.** `Generation of initial population`
* Random with verification of feasibility and evaluation
* Unfeasible individuals are discarded and new ones are generated
##
**7.** `Parent selection`
* Generational model
* From `dim` candidates we select `dim` parents
* We can use Stochastic Universal Sampling (SUS) Mechanism with FPS
* In this case without sigma scaling because the fitness can be negative
##
**8.** `Crossover`
* On population level
* Crossover probability pc > 0.5 (we can take 0.7 or 0.8)
* Any unfeasible individual is replaced with a clone of a parent
* For each pair of parents
    * Permutation representation: order matters
    * We use ordered crossover (OCX) for selecting remote islands in an ordered route
##
**9.** `Mutation`
* On population level
* General mutation scheme for problem with constraints
    * Probability of mutation pm is very low, usually 0.1
    * Any unfeasible individual is discarded and the mutation is cancelled for that individual
    * We use swap mutation
##
**10.** `Select next generation`
* Since we use a generational model we use `elitism`
##
**11.** `Stop condition`
* We stop the algorithm if:
    * We reach the limited number of steps
    * If fitness is the same for all generations
    * When optimum value is reached
    * If over the last k generations (given parameter) the fitness hasn't changed