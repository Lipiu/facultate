import numpy as np

# numerele de la 1 la 350 pot fi reprezentate pe 9 biti
#numbers in range 1..350 can be represented on 9 bits

# reprezentarea numarului natural x in sir binar Gray pe m biti
#Gray representation for natural number x on m bits
def nat_Gray(x,m):
    #obtine reprezentarea binara a lui x in forma '0b_sir de biti' si extrage sir_biti
    #standard binary representation of x (includes 0b at the begining of the string)
    t=bin(x)[2:]
    #completarea cu 0 pentru reprezentarea pe m biti
    #fill with 0 for m bits representation. t is a string of characters
    t=t.zfill(m)
    #t este un sir de caractere
    rezultat = t[0]
    for i in range(1,m):
        # efectuarea operatiei XOR la nivel de bit - lucreaza pe numere intregi
        #XOR on bits. XOR works only on integers
        bit= str(int(t[i]) ^ int(t[i-1]))
        # adaugarea la sir a caracterului bit
        #add character bit to the string
        rezultat=rezultat+bit
    # rezultatul este un sir de biti - string cu elemente '0' si '1'
    # the result is a string of characters, '0' and '1'
    return rezultat

# operatia inversa celei prezentate mai sus
# convert from Gray to integer
def Gray_bin(bG):
    m = len(bG)
    #obtine reprezentarea binara standard, ca sir de caractere
    #standard binary representation from Gray representation
    bS = bG[0]
    val=int(bG[0])
    for i in range(1,m):
        if bG[i]=='1':
            val=int(not(val))
        bS=bS+str(val)
    #obtine reprezentarea in baza 10 a sirului binar sir
    #base 10 representation of the binary string
    n = int(bS,2)
    return n

#fitness function
def fitness(sir):
    x=Gray_bin(sir)
    return x**2

#implementation for point a
def cerinta_a(dim):
    populatie=[]
    calitati=np.zeros(dim,dtype="int")
    for i in range(dim):
        x=np.random.randint(1,351)
        populatie=populatie+[nat_Gray(x,9)]
        calitati[i]=fitness(populatie[i])
    return np.array(populatie),calitati

#implementation for point b
#I:
# pop_c,qual_c,pop_mo,qual_mo - populatiile curenta si a copiilor mutati pe baza carora se face selectia, fiecare insotita de vectorii calitatilor
# dim, dimc - dimensiunile
#E: pop_r,qual_r - populatia rezultata si vectorul calitatilor
def cerinta_b(pop_c,qual_c,pop_mo,qual_mo,dim,dimc):
    #sortarea populatiei de copii in functie de calitati
    indici = np.argsort(qual_c)
    pops = pop_c[indici]
    quals = qual_c[indici]
    pop=pops.copy()
    qual=quals.copy()
    for i in range(dimc):
        pop[i]=pop_mo[i].copy()
        qual[i]=qual_mo[i]
    return pop,qual

if __name__=="__main__":
    dim_curent=10
    pop_curenta, qual_curenta=cerinta_a(dim_curent)
    print("POPULATIA CURENTA SI CALITATILE")
    print(pop_curenta)
    print(qual_curenta)
    dim_copiim = 2
    pop_copiim, qual_copiim = cerinta_a(dim_copiim)
    print("POPULATIA DE COPII MUTATI SI CALITATILE")
    print(pop_copiim)
    print(qual_copiim)
    rezultat,qual_rezultat=cerinta_b(pop_curenta,qual_curenta,pop_copiim,qual_copiim,dim_curent,dim_copiim)
    print("POPULATIA URMATOARE SI CALITATILE")
    print(rezultat)
    print(qual_rezultat)
