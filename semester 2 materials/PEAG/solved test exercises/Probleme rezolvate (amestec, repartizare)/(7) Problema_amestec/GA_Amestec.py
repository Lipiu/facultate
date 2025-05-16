import numpy as np
from Selectii import s_ruleta_SUS, s_elitista
from Recombinari import r_uniforma
import matplotlib.pyplot as grafic

masa_pachet=0.2         #masa unui pachet in kg

#definirea spatiului solutiilor
# individ - vector cu n componente x[i]= numărul de pachete din combinația i
# calculul numarului maxim de pachete/combinatie

def limite(combinatii,cantitati):
    #stabilirea domeniului de definitie pentru fiecare gena (nr. maxim pachete din fiecare tip)

    #I: combinatii - matrice combinatii
    #   cantitati - vector cantitati disponibile
    #E: limite_s - vector cu valorile maxime pentru fiecare gena

    nr_tipuri,nr_materii=np.shape(combinatii)
    limite_s=np.zeros(nr_tipuri)
    nr_produse=np.zeros(nr_materii)
    for i in range(nr_tipuri):
        #pt fiecare combinatie i, vectorul maximului de pachete in functie de materia prima folosita
        for j in range(nr_materii):
            if combinatii[i,j]:
                nr_produse[j]= cantitati[j] / (masa_pachet*combinatii[i,j]/100)
            else:
                nr_produse[j]=1000000       #fara limita daca materia j nu e folosita la tipul i
        limite_s[i]=int(np.min(nr_produse))
    return limite_s

def GA_Amestec(fprofit,fcomb,fcant, dim,nmax,pr,pm):
    #rezolvarea problemei de amestec

    #I: fprofit - fisier cu profituri pentru fiecare tip de pachet
    #   fcomb - fisier matrice combinatii materii prime pentru fiecare pachet
    #   fcant - fisier cantitai disponibile din fiecare materie prima
    #   dim - dimensiune populatie
    #   nmax - numar maxim de generatii permise
    #   pr - probabilitate de recombinare
    #   pm - probabilitate de mutatie
    #E: sol - rezultat calculat
    #   val - calitatea solutiei calculate
    #Exemplu de apel:
    #

    #preluare date din fisiere
    profit = np.genfromtxt(fprofit)
    combinatii = np.genfromtxt(fcomb)
    cantitati = np.genfromtxt(fcant)
    #stabilirea domeniului de definitie - spatiul solutiilor
    limite_s=limite(combinatii,cantitati)
    #generare populatie initiala
    pop=gen_pop_ini(profit,combinatii,cantitati,limite_s,dim)
    #initializari
    i=0
    divers=True
    FaraCrestere=0
    val=max(pop[:,-1])
    V=[val]
    #bucla de evolutie
    print("Muncesc...")
    while i<nmax and divers and FaraCrestere<nmax/3:
        if(i/10 == int(i/10)):
            print("Generatia ",i)
        #selectie parinti
        parinti=s_ruleta_SUS(pop)
        #recombinare
        desc=recombinare(parinti,pr, profit,combinatii,cantitati)
        #mutatie
        descm=mutatie(desc,pm,limite_s, profit,combinatii,cantitati)
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
    print("cu profitul ",val)
    consum=combinatii*masa_pachet/100
    nrtipuri,_=np.shape(combinatii)
    for i in range(nrtipuri):
        consum[i,:]*=sol[i]
    consum_total=np.sum(consum,0)
    print("Materii ramase neconsumate: ",cantitati-consum_total)
    arata(V)
    #trimitere rezultate
    return sol, val


def gen_pop_ini(profit,combinatii,cantitati,limite_s,dim):
    #generare populatie initiala

    #I: profit - vector profituri pe tipuri de pachete
    #   combinatii - matrice combinatii
    #   cantitati - vector cantitati disponibile
    #   limite_s - numar maxim de pachete din fiecare tip
    #   dim - dimensiune populatie
    #E: pop - matricea populatie, calitati pe ultima coloana (valori reale)

    nr_tipuri,_= np.shape(combinatii)
    pop=np.zeros((dim,nr_tipuri+1),dtype=float)
    i=0
    while i<dim:
        for j in range(nr_tipuri):
            pop[i,j]=np.random.randint(0,limite_s[j]+1)
        prof,viabil=f_obiectiv(pop[i,:-1],profit,combinatii,cantitati)
        if viabil:
            pop[i,-1]=prof
            i=i+1
    return pop

def f_obiectiv(x,profit,combinatii,cantitati):
    #functia de evaluare

    #I: x - individul evaluat
    #   profit - vector profituri pe tipuri de pachete
    #   combinatii - matrice combinatii
    #   cantitati - vector cantitati disponibile
    #E: c - calitatea calculata
    #   viabil - True daca respecta constringerile, False altfel

    nr_tipuri, nr_materii = np.shape(combinatii)
    c=np.dot(x,profit)
    #consum din fiecare materie
    consum_combinatii=masa_pachet*combinatii/100
    for i in range(nr_tipuri):
        consum_combinatii[i,:]*=x[i]
    total_consum_combinatii=np.sum(consum_combinatii,0)
    viabil=True
    i=0
    while i<nr_materii and viabil:
        if total_consum_combinatii[i]>cantitati[i]:
            viabil=False
        else:i+=1
    return c, viabil

def recombinare(parinti,pr, profit, combinatii, cantitati):
    #schema generala de recombinare

    #I: parinti - bazinul de parinti
    #   pr - probabilitatea de recombinare
    #   profit - vector profituri pe tipuri de pachete
    #   combinatii - matrice combinatii
    #   cantitati - vector cantitati disponibile
    #E: desc - descendenti creati

    dim,n=np.shape(parinti)
    desc=np.zeros((dim,n),dtype=float)
    #alegere aleatoare a perechilor de parinti
    perechi=np.random.permutation(dim)
    for i in range(0,dim,2):
        desc[i,:]=parinti[i,:]
        desc[i+1,:]=parinti[i,:]
        d1,d2,da=r_uniforma(desc[i,:-1],desc[i+1,:-1],pr)
        if da:
            calitate,viabil=f_obiectiv(d1,profit, combinatii, cantitati)
            if viabil:
                desc[i,:-1]=d1.copy()
                desc[i,-1]=calitate
            calitate, viabil = f_obiectiv(d2, profit, combinatii, cantitati)
            if viabil:
                desc[i+1,:-1]=d2.copy()
                desc[i+1,-1]=calitate
    return desc

def mutatie(desc,pm,limite_s, profit,combinatii,cantitati):
    #schema generala de mutatie

    #I: desc - descendentii obtinuti dupa recombinare
    #   pm - probabilitatea de mutatie
    #   profit - vector profituri pe tipuri de pachete
    #   combinatii - matrice combinatii
    #   cantitati - vector cantitati disponibile
    #E: descm - descendentii obtinuti dupa mutatie

    dim,_=np.shape(desc)
    descm=desc.copy()
    for i in range(dim):
        xm,da=m_int_fluaj(desc[i,:-1],pm,0,limite_s,1)
        if da:
            calitate,viabil=f_obiectiv(xm, profit, combinatii, cantitati)
            if viabil:
                descm[i,:-1]=xm.copy()
                descm[i,-1]=calitate
    return descm

#functie care implementeaza operatorul de mutatie fluaj pentru reprezentarea cu numere intregi este implementata
#in Mutatii.py in varianta in care domeniul de definitie este identic pentru toate genele.
#in aceasta problema domeniul este diferit pentru fiecare gena, de aceea mai jos
#este implementata o varianta in care limita superioara (b) este diferita pentru fiecare gena
def m_int_fluaj(x,pm,a,b,max):
    # operatorul de mutatie fluaj pentru intregi

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capete interval de definitie (aici b este vector)
    #    max - valoarea maxima de fluaj (modificare in intervalul [-max, max])
    # E: y - individ rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r = np.random.uniform(0, 1)
        if r<pm:
            da=1
            f=np.random.randint(-max, max+1)
            #pentru valori mari ale lui max: f=round(numpy.random.normal(0,max/3))
            y[i]=y[i]+f
            if y[i]<a:
                y[i]=a
            if y[i]>b[i]:   #limita superioara diferita pentru fiecare gena
                y[i]=b[i]
    return y, da

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
    s,v=GA_Amestec('profituri.txt','combinatii.txt','cantitati.txt',500,400,0.9,0.3)
    #s,v=GA_Amestec('profituri1.txt','combinatii1.txt','cantitati1.txt',5000,1000,0.9,0.3)


#Exemple de executie:
#s,v=GA_Amestec('profituri.txt','combinatii.txt','cantitati.txt',5000,1000,0.9,0.3)
#Rezultat calculat dupa:  1000  generatii noi
#[1250  138    0  184   90]
#cu profitul  29038.0


#s,v=GA_Amestec('profituri.txt','combinatii.txt','cantitati.txt',500,400,0.9,0.3)
#Rezultat calculat dupa:  400  generatii noi
#[1247   81    2  227  105]
#cu profitul  29029.0
#Materii ramase neconsumate:  [ 0.03 17.55  0.    0.02]

#SAU
#Rezultat calculat dupa:  400  generatii noi
#[1175  173   60  161   89]
#cu profitul  28507.0
#Materii ramase neconsumate:  [ 0.05 18.25  0.1   0.  ]


#s,v=G.GA_Amestec('profituri.txt','combinatii.txt','cantitati.txt',500,1000,0.9,0.3)
#Rezultat calculat dupa:  1000  generatii noi
#[1250  258    0   94   60]
#cu profitul  29008.0
#Materii ramase neconsumate:  [1.00000000e-01 1.75000000e+01 1.42108547e-14 0.00000000e+00]


#s,v=G.GA_Amestec('profituri.txt','combinatii.txt','cantitati.txt',2000,1000,0.9,0.3)
#Rezultat calculat dupa:  1000  generatii noi
#[1250   10    0  280  122]
#cu profitul  29070.0
#Materii ramase neconsumate:  [ 0.1 17.5  0.   0. ]

