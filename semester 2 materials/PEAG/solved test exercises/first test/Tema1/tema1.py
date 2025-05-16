import numpy as np

#fitness function
def fitness(p):
    n=len(p)
    val=0
    for i in range(n-1):
        for j in range(i+1,n):
            if p[i]==j and p[j]==i:
                val+=1
    return val

#implementation for point a
def cerinta_a(dim,n):
    pop=np.zeros([dim,n+1],dtype="int")
    for i in range(dim):
        pop[i,:n]=np.random.permutation(n)
        pop[i,n]=fitness(pop[i,:n])
    return pop

#mutation operator
def inserare(p):
    n=len(p)
    i=np.random.randint(0,n-1)
    j=np.random.randint(i+1,n)
    r=p.copy()
    r[i+1]=p[j]
    if i+1<j:
        r[i+2:j+1]=p[i+1:j]
    return r

#implementation for point b
def cerinta_b(pop,pm):
    dim=pop.shape[0]
    popm=pop.copy()
    for i in range(dim):
        r=np.random.uniform(0,1)
        if r<=pm:
            #print('Mutatie in ',pop[i,:-1], ' calitatea ',pop[i,-1])
            popm[i,:-1]=inserare(pop[i,:-1])
            popm[i,-1]=fitness(popm[i,:-1])
            #print('Rezulta    ',popm[i,:-1], ' calitatea ',popm[i,-1])
    return popm

if __name__=="__main__":
    n=20
    dim=10
    pm=0.2
    pop=cerinta_a(dim,n)
    print('Initial population:')
    print(pop)
    popm=cerinta_b(pop,pm)
    print('population after mutation')
    print(popm)