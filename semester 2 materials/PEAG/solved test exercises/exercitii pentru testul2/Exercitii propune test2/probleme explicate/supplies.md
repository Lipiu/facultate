## Supply problem (problem 5)
### Cerinta
In order to supply areas in distress with basic supplies, a humanitarian convoy is formed as a train with n
cars. The train will go through each area and unload supplies. The supplies are packed in m special
containers (m>>n). The mass for each container is known (can be read from a text file). Use a genetic
algorithm to find a way to distribute the containers into cars so that the mass is distributed as evenly as
possible. There is no upper mass limit for cars. 
##
**1.** `Inputs`
* DIM = dimension of the population
* N = number of train cars
* M = number of generations
* m = number of special containers
* Vectors
    * Mass of each container: Mass[i]
##
**2.** `Representation`
* Vector of integers m
* This is a problem with no constraints
##
**3.** `Solution space`
* The solution space is exponential
##
**4.** `Fitness`
* x: genotype --> vector assigning each container to a car
* Goal: distribution of the containers into cars so that the mass is distributed as evenly as possible
##
**5.** `Population model`
* Constant size over time 
* Generational model without constraints
##
**6.** `Generation of initial population`
* Random assignment
* All individuals are feasible
* We evaluate fitness upon generation
##
**7.** `Parent selection`
* Generational model
* From `dim` candidates we select `dim` parents
* We can use SUS with FPS without sigma scaling
##
**8.** `Crossover`
* On population level
* General crossover scheme for problems without constraints
* All individuals remain feasible
* Uniform crossover
* Crossover probability pc > 0.5 (usually 0.7 or 0.8)
##
**9.** `Mutation`
* On population level
* General mutation scheme for problems without constraints
* Probability of mutation is generally very low (0.1)
* All individuals remain feasible
* Operator: randomly assigns some containers to a different car
##
**10.** `Select next generation`
* Since we use a generational model we use elitism
##
**11.** `Stop condition`
* We reach the limited number of steps
* If fitness is the same for all generations
* When optimum value is reached
* If over the last k generations (given parameter) the fitness hasn't changed