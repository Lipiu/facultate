import numpy as np
from Selectii import s_ruleta_SUS, s_elitista
from Recombinari import r_uniforma
from Mutatii import m_int_ra
import matplotlib.pyplot as grafic


def GA_Vagoane(fdate, dim,nmax,pr,pm):
    #rezolvarea problemei incarcarii containerelor in vagoane

    #I: fdate - fisier cu datele de intrare (mase containere + numar vagoane (int)
    #   dim - dimensiune populatie
    #   nmax - numar maxim de generatii permise
    #   pr - probabilitate de recombinare
    #   pm - probabilitate de mutatie
    #E: sol - rezultat calculat
    #   val - calitatea solutiei calculate
    #Exemplu de apel:
    #   import GA_Vagoane as GV
    #   s,v=GV.GA_Vagoane("mase.txt",200, 300, 0.8, 0.1)
    # True
    # Rezultat calculat dupa:  246  generatii noi
    # [1 2 2 3 3 2 0 2 1 0 3 4 3 4 0 1 1 3 4 0]
    # cu calitatea  0.367584210922717
    # Incarcarea vagoanelor
    # [119. 119. 115. 120. 118.]
    # Diferenta maxima:  5.0

    #preluare date din fisier
    date=np.genfromtxt(fdate)
    mase=date[:-1]      #ultima valoare e numarul de vagoane
    nrv=int(date[-1])     #numarul de vagoane
    nrc=len(mase)         #numar de containere
    #generare populatie initiala
    pop=gen_pop_ini(nrv,nrc,mase,dim)
    #initializari
    i=0
    divers=True
    FaraCrestere=0
    val=max(pop[:,-1])
    V=[val]
    #bucla de evolutie
    while i<nmax and divers and FaraCrestere<nmax/3:
        #selectie parinti
        parinti=s_ruleta_SUS(pop)
        #recombinare
        desc=recombinare(parinti,pr,nrv,mase)
        #mutatie
        descm=mutatie(desc,pm,nrv,mase)
        #selectie generatia urmatoare
        pop=s_elitista(pop,descm)
        #operatii finale
        i=i+1
        val=max(pop[:,-1])
        if val==V[-1]:
            FaraCrestere+=1
        else:
            FaraCrestere=0
        V=V+[val]
        minim=min(pop[:,-1])
        divers= val!=minim
    #sfirsit bucla de evolutie
    print(divers)
    cine=pop[:,-1].argmax()
    sol=pop[cine,:-1].astype(int)
    #vizualizare evolutie si rezultate
    print("Rezultat calculat dupa: ",i," generatii noi")
    print(sol)
    print("cu calitatea ",val)
    vagoane = np.zeros(nrv, dtype=float)
    for j in range(nrc):
        vagoane[int(sol[j])] += mase[j]
    print("Incarcarea vagoanelor")
    print(vagoane)
    print("Diferenta maxima: ", max(vagoane) - min(vagoane) )
    arata(V)
    #trimitere rezultate
    return sol, val

def gen_pop_ini(nrv,nrc,mase,dim):
    #generare populatie initiala

    #I: nrv - numar vagoane
    #   nrc - numar containere
    #   dim - dimensiune populatie
    #E: pop - matricea populatie, calitati pe ultima coloana (valori reale)

    pop=np.zeros((dim,nrc+1),dtype=float)
    for i in range(dim):
        pop[i,:-1]=np.random.randint(0,nrv,nrc)
        pop[i,-1]=f_obiectiv(pop[i,:-1],nrv,mase)
    return pop

def f_obiectiv(x,n,mase):
    #functia de evaluare

    #I: x - individul evaluat
    #   n - numarul de vagoane
    #   mase - vector cu masele containerelor
    #E: c - calitatea calculata

    m=len(x)
    vagoane=np.zeros(n,dtype=float)
    for i in range(m):
        vagoane[int(x[i])]+=mase[i]
    c=1/(1+np.std(vagoane))
    #c=1/(1+np.max(vagoane)-np.min(vagoane))        #alternativa
    return c

def recombinare(parinti,pr,nrv,mase):
    #schema generala de recombinare

    #I: parinti - bazinul de parinti
    #   pr - probabilitatea de recombinare
    #   nrv - numar vagoane
    #   mase - mase containere (pentru evaluare
    #:  desc - descendenti obtinuti

    dim,n=np.shape(parinti)
    desc=np.zeros((dim,n),dtype=float)
    #alegere aleatoare a perechilor de parinti
    perechi=np.random.permutation(dim)
    for i in range(0,dim,2):
        desc[i,:]=parinti[i,:]
        desc[i+1,:]=parinti[i,:]
        d1,d2,da=r_uniforma(desc[i,:-1],desc[i+1,:-1],pr)
        if da:
            desc[i,:-1]=d1.copy()
            desc[i,-1]=f_obiectiv(d1,nrv,mase)
            desc[i+1,:-1]=d2.copy()
            desc[i+1,-1]=f_obiectiv(d2,nrv,mase)
    return desc

def mutatie(desc,pm,nrv,mase):
    #schema generala de mutatie

    #I: desc - descendentii obtinuti dupa recombinare
    #   pm - probabilitatea de mutatie
    #   nrv - numar vagoane
    #   mase - mase containere (pentru evaluare)
    #E: descm - descendentii obtinuti dupa mutatie

    dim,_=np.shape(desc)
    descm=desc.copy()
    for i in range(dim):
        xm,da=m_int_ra(desc[i,:-1],pm,0,nrv-1)
        if da:
            descm[i,:-1]=xm.copy()
            descm[i,-1]=f_obiectiv(xm,nrv,mase)
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
    #GA_Vagoane("mase.txt",200, 300, 0.8, 0.1)
    GA_Vagoane("mase1.txt",300, 500, 0.8, 0.1)