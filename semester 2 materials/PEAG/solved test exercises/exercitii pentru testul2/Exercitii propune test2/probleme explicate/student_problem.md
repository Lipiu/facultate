## Student problem

**1.** `Inputs of the student problem`
* Budget: 10000 units

* Courses:
    * course A
    * course B
    * course C

* Credit points:
    * course A - 5 credits
    * course B - 3 credits
    * course C - 8 credits

* Individual study hours required:
    * course A - 80 hours
    * course B - 40 hours
    * course C - 100 hours

**2.** `This is a problem with constraints`
* The constraints are:
    * the price of the combination of courses cannot exceed the available budget 
        * 1000a + 800b + 1500c <= 10000
    * the average individual study hours must be at most 70 (<70)
        $$
        \frac{80a + 40b + 100c}{a + b + c} <= 70
        $$
    * at least one course must be selected
        * a + b + c >= 0

If any of the constraints are violated, the individual is discarded and regenereated.

**3.** `Representation in solutions space`
* Chromosome: [a,b,c,FITNESS] where:
    * a = number of courses of type A
    * b = number of courses of type B
    * c = number of courses of type C
    * FITNESS = maximization of average credit points per course

**4.** `Solution space`
* Finite and discrete: number of possible combinations of courses that fit the budget (stay under or equal to budget).
* Each value of a, b and c is a non-negative integer.

**5.** `Fitness function`
* Objective: maximize average credit points per course.
* Fitness formula: $$
                    \frac{5a + 3b + 8c}{a + b + c}
                   $$
* if any constarint is not respected we apply a penalty.

**6.** `Population model`
* The population model is **Generational**, fixed-size population.

**7.** `Parent selection`
* We can use:
    1. Simple roulette
    2. Tournament selection

**8.** `Crossover operator`
* Uniform crossover or arithmetic crossover with:
    * Crossover rate = 0.7

**9.** `Mutation operator`
* Non-uniform mutation
    * We randomly increase/decrease a, b, or c by 1
    * Mutation rate = 0.2
    * Recheck constraint after mutation

**10.** `Survivor selection`
* Elitism: keep the best individual in next generation
* Remaining individuals are selected from offspring

**11.** `Stopping condition`
* Fixed number of generations
* No improvement in best fitness after n generations

