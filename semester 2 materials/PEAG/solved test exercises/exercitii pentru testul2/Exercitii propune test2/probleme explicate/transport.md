## Transportation problem (problem 4)

**1.** `Inputs`
* Factories and capacities
    * Bucuresti: Maximum production = 120 tons/week
    * Craiova: Maximum production = 140 tons/week

* Warehouses and demand
    * Ploiesti demand = 100 tons/week
    * Pitesti demand = 60 tons/week
    * Cluj demand = 80 tons/week

* Transport cost (per ton)
    * Bucuresti - Ploiesti = 50
    * Bucuresti - Pitesti = 70
    * Bucuresti - Cluj = 90
    * Craiova - Ploiesti = 60
    * Craiova - Pitesti = 70
    * Craiova - Cluj = 100
##
**2.** `Representation in solution space`
* We define the decision variables as the tons transported along each route, representing the solution as a vector of 6 elements:\
x = [xBP, xBPt, xBC, xCP, xCPt, xCC] where:
    * xBP = tons from Bucuresti to Ploiesti
    * xBPt = tons from Bucuresti to Pitesti
    * xBC = tons from Bucuresti to Cluj
    * xCP = tons from Craiova to Ploiesti
    * xCPt = tons from Craiova to Pitesti
    * xCC = tons from Craiova to Cluj

Each xi is a non-negative integer that represents the tonnage allocated for each route.
##
**3.** `Constraints`
* Production constraints
    * For Bucuresti
        * xBP + xBPt + xBC <= 120 (tons/week)
    * For Craiova
        * xCP + xCPt + xCC <= 140 (tons/week)
* Warehouse demand constraints
    * For Ploiesti
        * xBP + xCP <= 100 (tons/week)
    * For Pitesti
        * xBPt + xCPt <= 60 (tons/week)
    * For Cluj
        * xBC + xCC <= 80 (tons/week)
* Non-negativity
    * xi > 0 for all i
##
**4.** `Solution space`
* The solution space is a 6 dimensional discrete domain subject to the production and demand equality/inequality constraints.
##
**5.** `Fitness function`
* **Objective:** minimize the total transportation cost
* Transportation cost is computed as:
    * Total_cost = 50xBP + 70xBPt + 90xBC + 60xCP + 70xCPt + 100xCC
* For a feasbile solution, the fitness value is the total cost.
* Penalty
    * For each constraint violation we apply a penalty
##
**6.** `Population model`
* Generational model with fixed-size population
* Each individual represents a complete assignment of shipments
##
**7.** `Parent selection`
* Simple roulette selection
* We can also use tournament selection for simplicity
##
**8.** `Crossover operator`
* Uniform crossover: randomly swap elements between two parent vectors with a fixed crossover probability (for example: 0.7)

* After crossover it is important to re-check individuals to better satisfy the constraints.
##
**9.** `Mutation operator`
* Mutation: randomly adjust one or more components xi by a small integer (+/- 1) with a mutation probability (eg: 0.2)

* Repair/Constarint check: After mutation, recheck that the solution is as close as possible to meeting the warehouse demands and not exceeding factory capacities
##
**10.** `Survivor selection`
* Elitism to ensure the best solution (lowest cost) is kept in the next generation

* The rest of the next generation can be filled with offspring selected via generational replacement
##
**11.** `Stopping condition`
* Fixed number of generations

* Stop if the best fitness does not improve after n generations.

