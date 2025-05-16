import numpy as np
from Selectii import s_ruleta_SUS, s_elitista
from Recombinari import r_OCX
from Mutatii import m_perm_schimb
import matplotlib.pyplot as grafic


def GA_Ciini_pisici_permutari(m,n,dim,nmax,pr,pm):
    #rezolvarea problemei asezarii in cerc a n ciini si m pisici

    #I: n - numar ciini
    #   m - numar pisici
    #   dim - dimensiune populatie
    #   nmax - numar maxim de generatii permise
    #   pr - probabilitate de recombinare
    #   pm - probabilitate de mutatie
    #E: sol - rezultat calculat permutare
    #   val - calitatea solutiei calculate
    #Exemplu de apel:
    #   import GA_Ciini_pisici_permutari as G
    #   s,v,p=G.GA_Ciini_pisici_permutari(15,15,20,50,0.8,0.1)
    # Rezultat calculat dupa: 7  generatii noi
    # [20  5 26 29  4 13 22 15 16 11  3  0 12 19 28 23 10  6 27 24 25  9 14  2  8 17 18  1  7 21]
    # ['P', 'C', 'P', 'P', 'C', 'C', 'P', 'P', 'P', 'C', 'C', 'C', 'C', 'P', 'P', 'P', 'C', 'C', 'P', 'P', 'P', 'C', 'C', 'C', 'C', 'P', 'P', 'C', 'C', 'P']
    # cu calitatea  1.0

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
        desc=recombinare(parinti,pr,n)
        #mutatie
        descm=mutatie(desc,pm,n)
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
    sol_cp=["C" if sol[i]<n else "P" for i in range(n+m)]
    print(sol_cp)
    print("cu calitatea ",val)
    arata(V)
    #trimitere rezultate
    return sol, val, pop


def gen_pop_ini(n,m,dim):
    #generare populatie initiala; <n ciini, >=n pisica

    #I: n - numar ciini
    #   m - numar pisici
    #   dim - dimensiune populatien
    #E: pop - matricea populatie, calitati pe ultima coloana (valori reale)

    pop=np.zeros((dim,m+n+1),dtype=float)
    for i in range(dim):
        pop[i,:-1]=np.random.permutation(m+n)
        pop[i,-1]=f_obiectiv(pop[i,:-1],n)
    return pop

def f_obiectiv(x,n):
    #functia de evaluare

    #I: x - individul evaluat
    #   n - numarul de ciini
    #E: c - calitatea calculata

    l=len(x)
    cost=0
    for i in range(l-2):
        if x[i]<n and x[i+2]<n and x[i+1]>=n:
            cost=cost+1
    if x[l-2]<n and x[0]<n and x[l-1]>=n:
        cost=cost+1
    if x[l-1]<n and x[1]<n and x[0]>=n:
        cost=cost+1
    c=1/(1+cost)
    return c

def recombinare(parinti,pr,n):
    #schema generala de recombinare

    #I: parinti - bazinul de parinti
    #   pr - probabilitatea de recombinare
    #   m - numar de ciini (pentru evaluare)
    #:  desc - descendenti obtinuti

    dim,gene=np.shape(parinti)
    desc=np.zeros((dim,gene),dtype=float)
    #alegere aleatoare a perechilor de parinti
    perechi=np.random.permutation(dim)
    for i in range(0,dim,2):
        desc[i,:]=parinti[i,:]
        desc[i+1,:]=parinti[i,:]
        d1,d2,da=r_OCX(desc[i,:-1],desc[i+1,:-1],pr)
        if da:
            desc[i,:-1]=d1.copy()
            desc[i,-1]=f_obiectiv(d1,n)
            desc[i+1,:-1]=d2.copy()
            desc[i+1,-1]=f_obiectiv(d2,n)
    return desc

def mutatie(desc,pm,n):
    #schema generala de mutatie

    #I: desc - descendentii obtinuti dupa recombinare
    #   pm - probabilitatea de mutatie
    #   n - numar de ciini (pentru evaluare)
    #E: descm - descendentii obtinuti dupa mutatie

    dim,_=np.shape(desc)
    descm=desc.copy()
    for i in range(dim):
        xm,da=m_perm_schimb(desc[i,:-1],pm)
        if da:
            descm[i,:-1]=xm[:]
            descm[i,-1]=f_obiectiv(descm[i,:-1],n)
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


def verifica(pop,generatia):
    #verificarea calitatilor memorate in populatie

    dim,gene=np.shape(pop)
    print("Generatia ",generatia)
    for i in range(dim):
        if pop[i,-1]!=f_obiectiv(pop[i,:-1],15):
            print("Eroare la individul ",i)

if __name__=="__main__":
    s,v,p=GA_Ciini_pisici_permutari(15,15,20,50,0.8,0.1)