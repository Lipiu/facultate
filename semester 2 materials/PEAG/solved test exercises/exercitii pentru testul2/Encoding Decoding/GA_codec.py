import numpy
import matplotlib.pyplot as grafic
from Selectii import s_ruleta_SUS,s_elitista
from Recombinari import r_OCX
from Mutatii import m_perm_schimb

varianta=1          #varianta de functie de evaluare 1 / 2
#script=0            # 0 daca se ruleaza direct un exemplu, 1 daca se ruleaza scriptul Incercare.py

def GA_cod(fi, fo, dim, pr, pm, nmax, script=0):
    # determinarea modalitatii de codificare a unui mesaj

    # I: fi - fisier de intrare, cu mesajul original si cel codificat, pe cite o linie
    #    fo - fisier de iesire, cu corespondeta literelor
    #    dim - dimensiunea populatiei
    #    pr, pm - probabilitati de recombinare si mutatie
    #    nmax - numarul de generatii
    # E: sol - solutia gasita (permutare)
    #    v - calitatea solutiei (valoare functiei obiectiv) - 1 daca s-a gasit permutarea corecta
    # Exemplu de apel:
    #    mport GA_codec as GCDi
    #    s,v=GCD.GA_cod("CD_intrari.txt","CD_iesiri.txt",200,0.8,0.1,500)

    n = 26  # n=numar litere in alfabetul utilizat
    mesaj,cod=citire(fi)        # liste de valori numerice corespunzatoare literelor, fara repetare
    # generare populatie initiala
    pop = gen_pop(dim,n,mesaj,cod)
    # initializari
    fmax = max(pop[:,-1])
    vmax = [fmax]

    # bucla GA
    i = 0
    ok = True  # ok=True daca sint cel putin doua calitati diferite in populatie
    while i < nmax and ok and fmax<1:
        # selectie parinti
        parinti = s_ruleta_SUS(pop)
        # recombinare
        desc = recombinare(parinti,pr,mesaj,cod)
        # mutatie
        descm = mutatie(desc,pm,mesaj,cod)
        # selectie generatie urmatoare
        pop = s_elitista(pop, descm)
        # alte operatii
        # verifica diversitate genetica
        fmax = max(pop[:,-1])
        fmin = min(pop[:,-1])
        ok = fmax!=fmin
        # retine cea mai buna calitate
        vmax += [fmax]
        # retine cea mai buna solutie
        poz = numpy.argmax(pop[:, -1])
        sol = pop[poz][:n].astype(int)
        i += 1
    if not script:
        arata(sol, vmax)
        scrie_rezultate(sol,fo)
        verificare(fi,sol)
    return sol, vmax[-1]

def citire(fi):
    # preluare date din fisier text

    # I: fi - fisierul text din care se citesc mesajele (original si codificat)
    # E: m - mesaj original (necodificat)
    #    c - mesaj codificat
    #    ambele rezultate sint liste de valori numerice corespunzatoare literelor, fara repetare

    f = open(fi)
    m = f.readline()
    c = f.readline()
    f.close()
    m = m.rstrip()  #eliminare caractere albe de la sfirsitul sirului
    c = c.rstrip()
    m = [ord(m[i]) - ord('a') for i in range(len(m))]       # transformare in valori numerice
    c = [ord(c[i]) - ord('a') for i in range(len(c))]
    mesaj=list(dict.fromkeys(m))                            # eliminare dubluri
    cod=list(dict.fromkeys(c))
    return mesaj,cod

def f_obiectiv(x,mesaj,cod):
    # functia obiectiv

    # I: x - individ de evaluat
    #    mesaj - mesajul original, necodificat
    #    cod - mesaj codificat
    # E: c - calitate calculata

    c=0
    n=len(mesaj)
    for i in range(n):
        if varianta==1:
        # varianta 1: decodifica mesajul codificat si vezi cit de aproape de original este rezultatul
            k=list(x).index(cod[i])
            c+=abs(mesaj[i]-k)
        # varianta 2: codifica mesajul original si vezi cit de aproape de codificat este rezultatul
        else:
            c+=abs(cod[i]-x[mesaj[i]])
    return 1./(1+c)

def gen_pop(dim,n,mesaj,cod):
    # generare populatie de permutari cu n=26 elemente

    # I: dim - dimensiune populatie (nr. de indivizi)
    #    n - dimensiune individ (numar de lietere in alfabet)
    #    mesaj - mesajul original, necodificat
    #    cod - mesaj codificat
    # E: pop - populatia aleatoare generata, cu calitatea fiecarui individ pe ultima coloana

    pop=numpy.zeros((dim,n+1),dtype=float)
    for i in range(dim):
        pop[i,:n]=numpy.random.permutation(n)
        pop[i,n]=f_obiectiv(pop[i,:n],mesaj,cod)
    return pop

def recombinare(parinti,pr,mesaj,cod):
    # etapa de recombinare

    # I: parinti - parintii selectati
    #    pr - probabilitatea de recombinare
    #    mesaj - mesajul original, necodificat
    #    cod - mesaj codificat
    # E: desc - descendentii obtinuti

    dim, n = numpy.shape(parinti)
    desc = numpy.zeros((dim, n))
    # alegere aleatoare a perechilor de parinti
    perechi = numpy.random.permutation(dim)
    for i in range(0, dim, 2):
        x = parinti[perechi[i],:]
        y = parinti[perechi[i+1],:]
        d1, d2, da = r_OCX(x[:-1], y[:-1], pr)
        if da:
            desc[i, :-1] = d1
            desc[i][-1] = f_obiectiv(d1,mesaj,cod)
            desc[i+1, :-1] = d2
            desc[i+1][-1] = f_obiectiv(d2,mesaj,cod)
        else:
            desc[i,:]=x
            desc[i+1]=y
    return desc

def mutatie(desc,pm,mesaj,cod):
    # operatia de mutatie a descendentilor obtinuti din recombinare

    # I: desc - matricea descendentilor
    #    pm - probabilitatea de mutatie
    #    mesaj - mesajul original, necodificat
    #    cod - mesaj codificat
    # E: descm - matricea indivizilor obtinuti

    dim,_=numpy.shape(desc)
    descm=desc.copy()
    for i in range(dim):
        x=descm[i,:-1]
        y, da=m_perm_schimb(x,pm)
        if da:
            descm[i,:-1]=y
            descm[i][-1]=f_obiectiv(y,mesaj,cod)
    return descm

def arata(sol,v):
    # vizualizare rezultate

    # I: sol - permutarea care defineste drumul
    #    v - vectorul cu cea mai buna calitate din fiecare generatie
    # E: -

    cite = len(v)
    fig = grafic.figure()
    x = [k for k in range(cite)]
    grafic.plot(x, v, 'ro-')
    grafic.ylabel("Calitate")
    grafic.xlabel("Generația")
    grafic.title("Evoluția calității celui mai bun individ din fiecare generație")
    fig.show()
    print("\nCea mai bună permutare gasită: ",'\n  ['+' '.join(str(int(lit)) for lit in sol)+']')
    print("Cu costul: ", 1 / max(v)-1)

def scrie_rezultate(sol,fo):
    # scrie in fisier text corespondentele literelor utilizare pentru codificare

    # I: sol - permutarea solutie
    #    fo - numele fisierul rezultat

    n=26
    alfa=[chr(int(i+ord('a'))) for i in range(26)] + ["\n"]
    beta=[chr(int(sol[i]+ord('a'))) for i in range(26)] + ["\n"]
    f=open(fo,"w")
    f.write('  '.join(alfa))
    f.write('  '.join(beta))
    f.close()

def verificare(fi,sol):
    # verificarea permutarii gasite

    # I: fi - fisier de intrare, cu mesajul original si cel codificat, pe cite o linie
    #    sol - colutia gasita (permutare - cheie de codificare)

    print("TEST")
    f = open(fi)
    m = f.readline()
    c = f.readline()
    f.close()
    m = m.rstrip()
    c = c.rstrip()
    n=len(m)
    alfa = [chr(int(i + ord('a'))) for i in range(26)]
    codificat=[ alfa[int(sol[ord(m[i])-ord('a')])] for i in range(n)]
    print("mesaj     =",m)
    print("cod primit=",c)
    s=''.join(codificat)
    print("cod calc. =",s)
    if c==s:
        print("CORECT!")
    else:
        print("Nu e bine :(")


