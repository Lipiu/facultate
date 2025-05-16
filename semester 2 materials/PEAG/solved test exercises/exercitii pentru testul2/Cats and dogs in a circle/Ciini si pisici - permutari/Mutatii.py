import numpy

# operatori de mutatie
# binar: binar (negare)
# intregi: resetare aleatoare, fluaj
# reale: uniforma (r.a.), neuniforma (fluaj)
# permutari: interschimbare, inserare, inversare, amestec

def m_binar(x,pm):
    # operatorul de mutatie binara (negare) pentru reprezentarea binara

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    # E: y - individul rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r=numpy.random.uniform(0,1)
        if r<pm:
            da=1
            y[i]=1 if x[i]==0 else 0
    return y, da

def m_int_ra(x,pm,a,b):
    # operatorul de mutatie resetare aleatoare pentru intregi

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capete interval de definitie
    # E: y - individ rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r=numpy.random.uniform(0,1)
        if r<pm:
            da=1
            y[i]=numpy.random.randint(a,b+1)
    return y, da

def m_int_fluaj(x,pm,a,b,max):
    # operatorul de mutatie fluaj pentru intregi

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capete interval de definitie
    #    max - valoarea maxima de fluaj (modificare in intervalul [-max, max])
    # E: y - individ rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r = numpy.random.uniform(0, 1)
        if r<pm:
            da=1
            f=numpy.random.randint(-max, max+1)
            #pentru valori mari ale lui max: f=round(numpy.random.normal(0,max/3))
            y[i]=y[i]+f
            if y[i]<a:
                y[i]=a
            if y[i]>b:
                y[i]=b
    return y, da

def m_reale_unif(x,pm,a,b):
    # operatorul de mutatie uniforma pentru numere reale (resetare aleatoare)

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capete interval de definitie
    # E: y - individ rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y = x.copy()
    m = len(x)
    da=0
    for i in range(m):
        r = numpy.random.uniform(0, 1)
        if r < pm:
            da=1
            y[i] = numpy.random.uniform(a, b)
    return y, da

def m_reale_neunif(x,pm,a,b,max):
    # operatorul de mutatie neuniforma pentru numere reale (fluaj)

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capetele intervalului de definitie
    #    max - variatia maxima (fluaj in intervalul ([-max,max])
    # E: y - individul obtinut
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r=numpy.random.uniform(0,1)
        if r<pm:
            da=1
            f=numpy.random.normal(0,max/3)
            y[i]=y[i]+f
            if y[i]<a:
                y[i]=a
            if y[i]>b:
                y[i]=b
    return y, da

def m_reale_neunif2(x,pm,a,b,max):
    # operatorul de mutatie neuniforma pentru numere reale (fluaj)

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    #    a, b - capetele intervalului de definitie (cite un interval pentru fiecare gena)
    #    max - variatia maxima (fluaj in intervalul ([-max,max], cite un interval pt. fiecare gena)
    # E: y - individul obtinut
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    m=len(x)
    da=0
    for i in range(m):
        r=numpy.random.uniform(0,1)
        if r<pm:
            da=1
            f=numpy.random.normal(0,max[i]/3)
            y[i]=y[i]+f
            if y[i]<a[i]:
                y[i]=a[i]
            if y[i]>b[i]:
                y[i]=b[i]
    return y, da

def m_perm_schimb(x,pm):
    # operatorul de mutatie prin interschimbare pentru permutari

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    # E: y - individul rezultat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    r=numpy.random.uniform(0,1)
    da=0
    if r<pm:
        da=1
        m = len(x)
        p = numpy.random.randint(0, m, 2)
        while p[0] == p[1]:
            p[1] = numpy.random.randint(0,m)
        y[p[1]]=x[p[0]]
        y[p[0]]=x[p[1]]
    return y, da

def m_perm_inserare(x,pm):
    # operatorul de mutatie prin inserare pentru permutari

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    # E: y - individul modificat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    r=numpy.random.uniform(0,1)
    da=0
    if r<pm:
        da=1
        m=len(x)
        p=numpy.random.randint(0,m,2)
        while p[0] == p[1]:
            p[1] = numpy.random.randint(0,m)
        p.sort(); i=p[0]; j=p[1]
        y[i+2:j+1]=x[i+1:j]
        y[i+1]=x[j]
    return y, da

def m_perm_amestec(x,pm):
    # operatorul de mutatie prin amestec pentru permutari

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    # E: y - individul modificat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y = x.copy()
    r = numpy.random.uniform(0, 1)
    da=0
    if r < pm:
        da=1
        m = len(x)
        i=numpy.random.randint(m-1)
        j=numpy.random.randint(i+1,m)
        #amestec=numpy.random.permutation(j-i+1)
        #for k in range(j-i+1):
        #   y[i+amestec[k]]=x[i+k]
        numpy.random.shuffle(y[i:j+1])
    return y, da

def m_perm_inversiune(x,pm):
    # operatorul de mutatie prin inversiune pentru permutari

    # I: x - individul supus mutatiei
    #    pm - probabilitatea de mutatie
    # E: y - individul modificat
    #    da - 1 daca s-a produs mutatie, 0 daca y este chiar x

    y=x.copy()
    r=numpy.random.uniform(0,1)
    da=0
    if r<pm:
        da=1
        m=len(x)
        p=numpy.random.randint(0,m,2)
        while p[0] == p[1]:
            p[1] = numpy.random.randint(0,m)
        p.sort()
        y[p[0]:p[1]+1]=[x[i] for i in range(p[1],p[0]-1,-1)]
    return y, da
