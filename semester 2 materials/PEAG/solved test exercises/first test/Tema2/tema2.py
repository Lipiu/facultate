import numpy as np

#reprezentare n pe m biti prin sir binar memorat ca vector de 0-1
#decimal to binary: represent n on m bits as binary list
def dec_to_bin(n,m):
    #reprezentare standard, dar prin sir de caractere
    #standard binary representation, but as string of characters
    repr = bin(n)[2:]
    #transformare in string de m caractere
    #transform into string of m characters by adding 0s to the left
    repr_f = repr.zfill(m)
    #transformare in sir binar
    #transform into binary list of integers
    x=[int(repr_f[i]) for i in range(m)]
    return x

#binary to decimal transformation
def bin_to_dec(x,m):
    #transfer din lista de int in lista de caractere
    #transfer from list of integers into list of characters
    y=''
    for i in range(m):
        y+=str(x[i])
    #reprezentarea in baza 10
    #convert to decimal
    n=int(y,2)
    return n

#functia fitness
def fitness(sir):
    x=bin_to_dec(sir[0:11],11)
    y=bin_to_dec(sir[11:23],12)
    return (y-1)*(np.sin(x-2)**2)

#implementation for point a
#un individ are 23 biti - reprezentarea binara a numerelor din {1,...,1500} concatenata cu
# reprezentarea binara a numerelor din {0,...,2501}
#a chromosome consists of 23 bits - binary representation of numbers from {1,...,1500}
# concatenated with binary representation of numbers from {0,...,2501}
def cerinta_a(dim):
    pop=[]
    #print("POPULATIA INITIALA")
    for i in range(dim):
        x=np.random.randint(0,1501)
        y=np.random.randint(0,2502)
        print("Componentele in baza 10 (fenotipul):",x,y)
        individ=dec_to_bin(x,11)+dec_to_bin(y+1,12)
        print("Reprezentarea genotipului",individ)
        calitate=fitness(individ)
        print("Fitness:",calitate)
        individ=individ+[calitate]
        pop=pop+[individ]
    return pop

# 3 points crossover
def recombinare_3puncte(sir1,sir2):
    n=23
    i=np.random.randint(0,n-2)
    j=np.random.randint(i+1,n-1)
    k=np.random.randint(j+1,n)
    #print(i,j,k)
    copil1=sir1.copy()
    copil2=sir2.copy()
    copil1[j:k+1]=sir2[j:k+1]
    copil2[j:k+1]=sir1[j:k+1]
    return copil1, copil2

#implementation for point b
def cerinta_b(pop,pc):
    #print("\n\nPOPULATIA DE COPII")
    dim=len(pop)
    copii=pop.copy()
    for i in range(0,dim-1,2):
        r=np.random.uniform(0,1)
        if r<=pc:
            #selectarea indivizilor, fara calitatile lor
            p1=pop[i][:23].copy()
            p2=pop[i+1][:23].copy()
            c1,c2=recombinare_3puncte(p1,p2)
            copii[i][:23]=c1
            copii[i][23]=fitness(c1)
            copii[i+1][:23] = c2
            copii[i+1][23] = fitness(c2)
        #print("Individ+calitate",copii[i])
        #print("Individ+calitate", copii[i+1])
    return copii

if __name__=="__main__":
    pop=cerinta_a(10)
    print('Initial population:')
    print(pop)
    popc=cerinta_b(p,0.8)
    print('Descendants:')
    print(popc)


