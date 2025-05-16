import numpy

# operatori de recombinare
# binar, intregi, reale: unipunct, multipunct, uniforma
# reale: aritmetica singulara, simpla, totala
# permutari: OCX, PMX, CX

def r_unipunct(x,y,pr):
    # operatorul de recombinare unipunct

    # I: x, y - indivizi care se recombina
    #    pr - probabilitatea de recombinare
    # E: a, b - descendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()      #a=x[:]
    b=y.copy()
    da=0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da=1
        m=len(x)
        poz=numpy.random.randint(m)
        a[poz:m]=y[poz:m]
        b[poz:m]=x[poz:m]
    return a, b, da

def r_unipunct2(x,y,pr):
    # operatorul de recombinare unipunct pentru indivizi cu 2 gene

    # I: x, y - indivizi care se recombina
    #    pr - probabilitatea de recombinare
    # E: a, b - descendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()
    b=y.copy()
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        a[1]=y[1]
        b[1]=x[1]
    return a,b,da

def r_multipunct(x,y,pr,n):
    # operatorul de recombinare multipunct

    # I: x, y - cromozomi care se recombina
    #    pr - probabilitatea de recombinare
    #    n - numarul de puncte de recombinare
    # E: a, b - recendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a = x.copy()
    b = y.copy()
    da = 0
    r = numpy.random.uniform(0, 1)
    if r < pr:
        da = 1
        m = len(x)
        p=[]
        for i in range(n):
            poz=numpy.random.randint(m)
            while poz in p:
                poz = numpy.random.randint(m)
            p.append(poz)
        p.sort()
        if n % 2 == 1:
            p.append(m)
        for i in range(0,n,2):
            a[p[i]:p[i+1]]=y[p[i]:p[i+1]]
            b[p[i]:p[i+1]]=x[p[i]:p[i+1]]
    return a,b,da

def r_uniforma(x,y,pr):
    # operatorul de recombinare uniforma (toate pozitiile)

    # I: x, y - cromozomi care se recombina
    #    pr - probabilitatea de recombinare
    # E: a, b - recendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a = x.copy()
    b = y.copy()
    m = len(x)
    da = 0
    r = numpy.random.uniform(0, 1)
    if r < pr:
        for i in range(m):
            r = numpy.random.uniform(0, 1)
            if r < 0.5:         #conform manual, Syswerda 1989
                da = 1
                a[i]=y[i]
                b[i]=x[i]
    return a,b,da

def r_a_simpla(x,y,pr,w):
    # operatorul de recombinare aritmetica simpla (nr. reale)

    # I: x, y - parinti
    #    pr - probabilitatea de recombinare
    #    w - pondere
    # E: a, b - descendenti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()
    b=y.copy()
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        poz=numpy.random.randint(m)
        a[poz:m] = (1 - w) * x[poz:m] + w * y[poz:m]
        b[poz:m] = (1 - w) * y[poz:m] + w * x[poz:m]
    return a,b,da

def r_a_sing(x,y,pr,w):
    # operatorul de recombinare aritmetica singulara (nr. reale)

    # I: x, y - parinti
    #    pr - probabilitatea de recombinare
    #    w - pondere
    # E: a, b - descendenti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()
    b=y.copy()
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        poz=numpy.random.randint(m)
        a[poz] = (1 - w) * x[poz] + w * y[poz]
        b[poz] = (1 - w) * y[poz] + w * x[poz]
    return a,b,da

def r_a_total(x,y,pr,w):
    # operatorul de recombinare aritmetica totala (nr. reale)

    # I: x, y - parinti
    #    pr - probabilitatea de recombinare
    #    w - pondere
    # E: a, b - descendenti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()
    b=y.copy()
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        a = (1 - w) * x + w * y
        b = (1 - w) * y + w * x
    return a,b,da

def r_OCX(x,y,pr):
    # operatorul de recombinare Order Crossover pentru indivizi permutari

    # I: x, y - indivizi care se recombina (permutari)
    #    pr - probabilitatea de recombinare
    # E: a, b - descendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x[:]
    b=y[:]
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        p=numpy.random.randint(0,m,2)
        while p[0]==p[1]:
            p[1]=numpy.random.randint(m)
        p.sort()
        a=OCX(x,y,p)
        b=OCX(y,x,p)
    return a,b,da

def OCX(x,y,p):
    # generarea unui descendent conform Order Crossover

    # I: x, y - parinti
    #   p - vector cu cele 2 pozitii
    # E: d - descendentul creat

    m=len(x)
    d=numpy.zeros(m,dtype=int)-1
    d[p[0]:p[1]+1]=x[p[0]:p[1]+1]
    unde=p[1]+1
    for i in [k for k in range(p[1],m)]+[k for k in range(p[1])]:
        if not(y[i] in d):
            if unde>=m:
                unde=0
            d[unde]=y[i]
            unde+=1
    return d

def r_PMX(x,y,pr):
    # operatorul de recombinare Partially Mapped Crossover pentru indivizi permutari

    # I: x, y - indivizi care se recombina (permutari)
    #    pr - probabilitatea de recombinare
    # E: a, b - descendenti obtinuti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x[:]
    b=y[:]
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        p=numpy.random.randint(0,m,2)
        while p[0]==p[1]:
            p[1]=numpy.random.randint(m)
        p.sort()
        a=PMX(x,y,p)
        b=PMX(y,x,p)
    return a,b, da

def PMX(x,y,p):
    # generarea unui descendent conform Partially Mapped Crossover

    # I: x, y - parinti
    #   p - vector cu cele 2 pozitii
    # E: d - descendentul creat

    m=len(x)
    d=numpy.zeros(m,dtype=int)-1
    d[p[0]:p[1]+1]=x[p[0]:p[1]+1]
    for k in range(p[0], p[1] + 1):
        if not (y[k] in d):
            i = numpy.where(y == d[k])
            while d[i[0][0]] != -1:
                i = numpy.where(y == d[i[0][0]])
            d[i[0][0]] = y[k]
    for i in range(m):
        if not (y[i] in d):
            d[i] = y[i]
    return d

def r_CX(x,y,pr):
    # operatorul de recombinare Cycle Crossover pentru permutari

    # I: x,y - cromozomii parinti
    #    pr - probabilitatea de recombinare
    # E: a,b - descendenti
    #    da - 1 daca se creaza indivizi noi, 0 altfel

    a=x.copy()
    b=y.copy()
    da = 0
    r=numpy.random.uniform(0,1)
    if r<pr:
        da = 1
        m=len(x)
        c,nrc=cicluri(x,y)
        for t in range(1,nrc+1,2):
            for i in range(m):
                if c[i]==t:
                    a[i]=y[i]
                    b[i]=x[i]
    return a, b, da

def cicluri(x,y):
    # determinare cicluri pentru CX

    # I: x, y - cromozomi
    # E: c - vector cu indicii ciclurilor
    #    cite - numarul de cicluri

    m=len(x)
    c=numpy.zeros(m,dtype=int)
    continua=1
    i=0
    cite=1
    while continua:
        a=y[i]
        c[i]=cite
        while x[i]!=a:
            j=list(x).index(a)
            c[j]=cite
            a=y[j]
        try:
            i=list(c).index(0)
            cite+=1
        except:
            continua=0
    return c,cite