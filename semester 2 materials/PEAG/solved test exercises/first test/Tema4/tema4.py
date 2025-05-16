import numpy as np

#fitness fucntion
def fitness(x):
    return 1+np.sin(2*x[0]-x[2])+np.cos(x[1])

#implementation for point a
def cerinta_a(dim):
    pop=np.zeros([dim,4])
    for i in range(dim):
        pop[i, 0]=np.random.uniform(-1,1)
        pop[i, 1] = np.random.uniform(0, 1)
        pop[i, 2] = np.random.uniform(-2, 1)
        pop[i,3]=fitness(pop[i,:3])
    return pop

#total arithmetic crossover
def aritmetica_t(x,y,alpha):
    r1=alpha*x+(1-alpha)*y
    r2=alpha*y+(1-alpha)*x
    return r1,r2

#point b implementation
#the crossover is applied on pairs of consecutive individuals from pop
def cerinta_b(pop,pc,alpha):
    dim=pop.shape[0]
    popc=pop.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        if r<=pc:
            #print('\nCrossover in \n',pop[i,:-1], ' calitatea ',pop[i,-1],'\n',pop[i+1,:-1], ' calitatea ',pop[i+1,-1])
            popc[i,:-1],popc[i+1,:-1]=aritmetica_t(pop[i,:-1],pop[i+1,:-1],alpha)
            popc[i,-1]=fitness(popc[i,:-1])
            popc[i+1,-1]=fitness(popc[i+1,:-1])
            #print('Rezulta\n',popc[i,:-1], ' calitatea ',popc[i,-1],'\n',popc[i+1,:-1], ' calitatea ',popc[i+1,-1])
    return popc

if __name__=="__main__":
    dim=10
    pc=0.7
    alpha=0.25
    pop=cerinta_a(dim)
    print('Initial population:')
    print(pop)
    popc=cerinta_b(pop,pc,alpha)
    print('Crossover descendants:')
    print(popc)
