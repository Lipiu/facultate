import numpy

# distributii: FPS, FPS_ss, rang_l, rang_e
# selectii: ruleta, ruleta_SUS, elitista, superelitista, genitor, turneu2, turneu

def d_FPS(pop):
    # distributia de selectie FPS

    # I: pop - bazinul de selectie
    # E: p - vector probabilitati de selectie individuale
    #    q - vector probabilitati de selectie cumulate

    m, n = numpy.shape(pop)
    p=pop[:,n-1]
    s=numpy.sum(p)
    p=p/s
    q = [numpy.sum(p[:i + 1]) for i in range(m)]
    return p, q

def d_FPS_ss(pop,c):
    # distributia de selectie FPS cu sigma scalare

    # I: pop - bazinul de selectie
    #    c - constanta din formula de ajustare. uzual: 2
    # E: p - vector probabilitati de selectie individuale
    #    q - vector probabilitati de selectie cumulate

    m,n=numpy.shape(pop)
    medie=numpy.mean(pop[:,n-1])
    sigma=numpy.std(pop[:,n-1])
    val=medie-c*sigma
    g=[numpy.max([0, pop[i][n-1]-val]) for i in range(m)]
    s=numpy.sum(g)
    p=g/s
    q=[numpy.sum(p[:i+1]) for i in range(m)]
    return p,q

def d_rang_l(m,s):
    # distributia de selectie tip rang liniar

    # I: m - dimensiunea bazinului de selectie
    #    s - constanta 2 pentru rangul liniar: [1.0, 2.0]
    # E: p - vector probabilitati de selectie individuale
    #    q - vector probabilitati de selectie cumulate

    p=[(2-s)/m+2*(i+1)*(s-1)/(m*(m+1)) for i in range(m)]
    #daca se foloseste formula cu minus:
    #s=numpy.sum(p)
    #p=p/s
    q = [numpy.sum(p[:i + 1]) for i in range(m)]
    return p,q

def d_rang_e(m):
    # distributia de selectie tip rang exponential

    # I: m - dimensiunea bazinului de selectie
    # E: p - vector probabilitati de selectie individuale
    #    q - vector probabilitati de selectie cumulate

    p=[1-numpy.exp(-i) for i in range(m)]
    c=numpy.sum(p)
    p=p/c
    q = [numpy.sum(p[:i + 1]) for i in range(m)]
    return p, q

def s_ruleta(pop):
    # selectia tip ruleta simpla (un brat)

    # I: pop - bazinul de selectie
    # E: rez - populatia selectata

    m, n = numpy.shape(pop)
    p, q = d_FPS_ss(pop, 2)  # sau alta distributie
    rez = numpy.zeros((m, n), dtype=int)
    for k in range(m):
        r = numpy.random.uniform(0, 1)
        i=0
        while i<m-1 and r>q[i]:
            i+=1
        rez[k,:]=pop[i,:]
    return rez

def s_ruleta_SUS(pop):
    # selectia tip ruleta multibrat

    # I: pop - bazinul de selectie
    # E: rez - populatia selectata

    m,n=numpy.shape(pop)
    p,q=d_FPS_ss(pop,2)                 #sau alta distributie
    rez=pop.copy()
    i=0
    k=0
    r=numpy.random.uniform(0,1/m)
    while k<m:
        while r<=q[i]:
            rez[k,:n]=pop[i,:n]
            r+=1/m
            k+=1
        i+=1
    return rez

def s_elitista(pop,desc):
    # selectia elitista a generatiei urmatoare

    # I: pop - populatia curenta
    #    desc - descendentii populatiei curente
    # E: noua - matricea descendentilor selectati

    noua=desc.copy()
    dim,n=numpy.shape(pop)
    max1=max(pop[:,n-1])
    i=numpy.argmax(pop[:,n-1])
    max2=max(desc[:,n-1])
    if max1>max2:
        k=numpy.argmin(desc[:,n-1])
        noua[k,:]=pop[i,:]
    return noua

def s_superelitista(pop,desc):
    # selectia superelitista a generatiei urmatoare

    # I: pop - populatia curenta
    #    desc - descendentii populatiei curente
    # E: noua - matricea descendentilor selectati

    dim, m = numpy.shape(pop)
    b=numpy.vstack((pop,desc))
    bs=b[b[:,m-1].argsort()]
    noua=bs[dim:2*dim,:]
    return noua

def s_turneu2(pop):
    # selectie tip turneu

    # I: pop - populatia curenta
    # E: rez - indivizi selectati ca parinti

    dim,m=numpy.shape(pop)
    rez=numpy.zeros(shape=(dim,m))
    for i in range (dim):
        p=numpy.random.randint(0,dim,2)
        if pop[p[0],m-1]>pop[p[1],m-1]:
            rez[i,:]=pop[p[0],:]
        else:
            rez[i,:]=pop[p[1],:]
    return rez

def s_turneu(pop,k,nr):
    # selectie tip turneu de dimensiune data

    # I: pop - populatia curenta
    #    k - dimensiune turneu
    #    nr - numarul de indivizi selectati (dim pentru parinti, dim/2 pentru generatia urmatoare)
    # E: parinti - indivizi selectati ca parinti

    dim, _ = numpy.shape(pop)
    rez = numpy.zeros((nr, m))
    for i in range(nr):
        turneu=numpy.random.randint(0,dim,k)
        valori=[pop[turneu[i]][-1] for i in range(k)]
        cine=numpy.argmax(valori)
        rez[i,:]=pop[turneu[cine],:]
    return rez

def s_genitor(pop,desc,nr):
    # selectie de tip genitor

    # I: pop - populatia curenta
    #    desc - descendentii populatiei curente
    #    nr - numarul de indivizi care se inlocuiesc
    # E: noua - populatia noua (supravietuitorii)

    dim,m=numpy.shape(pop)
    b1=pop[pop[:,m-1].argsort()]
    b2=desc[-desc[:,m-1].argsort()]
    noua=b1.copy()
    noua[0:nr,:]=b2[0:nr,:]
    return noua

