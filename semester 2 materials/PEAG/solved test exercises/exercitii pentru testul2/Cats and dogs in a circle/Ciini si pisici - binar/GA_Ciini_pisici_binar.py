import numpy as np
from Selectii import s_ruleta_SUS, s_elitista
from Recombinari import r_unipunct
from Mutatii import m_binar
import matplotlib.pyplot as grafic


def GA_Ciini_pisici_binar(m,n,dim,nmax,pr,pm):
    #rezolvarea problemei asezarii in cerc a n ciini si m pisici

    #I: n - numar ciini
    #   m - numar pisici
    #   dim - dimensiune populatie
    #   nmax - numar maxim de generatii permise
    #   pr - probabilitate de recombinare
    #   pm - probabilitate de mutatie
    #E: sol - rezultat calculat (sir binar)
    #   val - calitatea solutiei calculate
    #Exemplu de apel:
    #   import GA_Ciini_pisici_binar as G
    #   s,v=G.GA_Ciini_pisici_binar(10,15,20,50,0.8,0.1)
    #   Rezultat calculat dupa: 14  generatii noi
    #   [1 1 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 1 1 1 1 1 0 0 1]
    #   cu calitatea  1.0

    #generare populatie initiala
    pop=gen_pop_ini(n,m,dim)
    #initializari
    i=0
    divers=True
    val=max(pop[:,-1])
    V=[val]
    #bucla de evolutie
    while i<nmax and divers and val<1:
        #selectie parinti
        parinti=s_ruleta_SUS(pop)
        #recombinare
        desc=recombinare(parinti,pr,m)
        #mutatie
        descm=mutatie(desc,pm,m)
        #selectie generatia urmatoare
        pop=s_elitista(pop,descm)
        #operatii finale
        i=i+1
        val=max(pop[:,-1])
        V=V+[val]
        minim=min(pop[:,-1])
        divers= val!=minim
    #sfirsit bucla de evolutie
    cine=pop[:,-1].argmax()
    sol=pop[cine,:-1].astype(int)
    #vizualizare evolutie si rezultate
    print("Rezultat calculat dupa:",i," generatii noi")
    print(sol)
    print("cu calitatea ",val)
    arata(V)
    #trimitere rezultate
    return sol, val


def gen_pop_ini(n,m,dim):
    #generare populatie initiala; 1 - pisica, 0 - ciine

    #I: n - numar ciini
    #   m - numar pisici
    #   dim - dimensiune populatie
    #E: pop - matricea populatie, calitati pe ultima coloana (valori reale)

    pop=np.zeros((dim,m+n+1),dtype=float)
    for i in range(dim):
        pop[i,:-1]=np.random.randint(0,2,m+n)
        pop[i,-1]=f_obiectiv(pop[i,:-1],m)
    return pop

def f_obiectiv(x,m):
    #functia de evaluare

    #I: x - individul evaluat
    #   m - numarul de pisici
    #E: c - calitatea calculata

    l=len(x)
    cost=0
    for i in range(l-2):
        if x[i]==0 and x[i+2]==0 and x[i+1]==1:
            cost=cost+1
    if x[l-2]==0 and x[0]==0 and x[l-1]==1:
        cost=cost+1
    if x[l-1]==0 and x[1]==0 and x[0]==1:
        cost=cost+1
    cost=cost+abs(m-sum(x))
    c=1/(1+cost)
    return c

def recombinare(parinti,pr,m):
    #schema generala de recombinare

    #I: parinti - bazinul de parinti
    #   pr - probabilitatea de recombinare
    #   m - numar de pisici (pentru evaluare)
    #:  desc - descendenti obtinuti

    dim,n=np.shape(parinti)
    desc=np.zeros((dim,n),dtype=float)
    #alegere aleatoare a perechilor de parinti
    perechi=np.random.permutation(dim)
    for i in range(0,dim,2):
        desc[i,:]=parinti[i,:]
        desc[i+1,:]=parinti[i,:]
        d1,d2,da=r_unipunct(desc[i,:-1],desc[i+1,:-1],pr)
        if da:
            desc[i,:-1]=d1.copy()
            desc[i,-1]=f_obiectiv(d1,m)
            desc[i+1,:-1]=d2.copy()
            desc[i+1,-1]=f_obiectiv(d2,m)
    return desc

def mutatie(desc,pm,m):
    #schema generala de mutatie

    #I: desc - descendentii obtinuti dupa recombinare
    #   pm - probabilitatea de mutatie
    #   m - numar de pisici (pentru evaluare)
    #E: descm - descendentii obtinuti dupa mutatie

    dim,n=np.shape(desc)
    descm=desc.copy()
    for i in range(dim):
        xm,da=m_binar(desc[i,:-1],pm)
        if da:
            descm[i,:-1]=xm.copy()
            descm[i,-1]=f_obiectiv(xm,m)
    return descm

def arata(V):
    #vizualizare evolutie calitate

    #I: V - lista cu cea mai buna calitate din fiecare generatie
    #E: -

    fig=grafic.figure()
    x=[int(V[i]) for i in range(len(V))]
    y=[i for i in range(len(V))]
    grafic.plot(y,V,"r-")
    grafic.xlabel("Generația")
    grafic.ylabel("Calitate")

if __name__=="__main__":
    GA_Ciini_pisici_binar(5,6,20,50,0.8,0.1)