# Script pentru testare exemplu codificare-decodificare
# Pentru fiecare exemplu
#   ruleaza de mai multe ori
#   numara de cite ori s-a terminat cu identificarea solutiei corecte
#   calculeaza timpul de executie: minim, mediu, maxim
#   afiseaza rezultate
#
# Inainte de a rula scriptul, elimina (comenteaza) apelul functiei `arata` din GA_codec.py
# pentru a evita deschiderea unui numar foarte mare de ferestre grafice

import numpy as np
import GA_codec as GCD
import datetime

n_e=3               #numar exemple de test
# lista perechi de fisiere: [date de test, fisier rezultate]
exemple=[['CD_intrari.txt', 'CD_iesiri.txt'],
         ['CD_intrari1.txt', 'CD_iesiri1.txt'],
         ['CD_intrari2.txt', 'CD_iesiri2.txt']]

repetari=10         #numar de repetari pentru fiecare set de date de test

rezultate=np.zeros((n_e, repetari, 3))    # pe fiecare linie: calitate rezultat, succes(0/1), timp
succes=np.zeros(n_e)

d_p=100     #dimensiune populatie
p_r=0.8     #probabilitate recombinare
p_m=0.1     #probabilitate mutatie
n_i=250     #numar iteratii
script=1    # 0 daca se ruleaza direct un exemplu, 1 daca se ruleaza scriptul Incercare.py


for i in range(n_e):                #pentru fiecare exemplu de test
    for j in range(repetari):       #ruleaza repetat
        print('Exemplul', i, 'incercarea', j)
        timp_inceput = datetime.datetime.now()
        s, v = GCD.GA_cod(exemple[i][0], exemple[i][1], d_p, p_r, p_m, n_i, script)
        durata = datetime.datetime.now() - timp_inceput
        rezultate[i,j,0]=v
        if v==1:
            rezultate[i,j,1]=1
        rezultate[i,j,2]=durata.total_seconds()
        print('A durat',durata.total_seconds(),'secunde')
    #terminare repetari

    #vizualizare rezultate pentru exemplul curent
    succes[i]=sum(rezultate[i,:,1])
    timp_minim=min(rezultate[i,:,2])
    timp_maxim=max(rezultate[i,:,2])
    timp_mediu=np.mean(rezultate[i,:,2])
    print('Exemplul de test',i,'\n')
    print('Succes in',succes[i],'incercari din',repetari,'(',succes[i]/repetari*100,'%)')
    print('Timp: minim -',timp_minim,'mediu -',timp_mediu,'maxim - ',timp_maxim)
    print('\n\n')

#rezultat final
print('Rezultate dupa',repetari,'incercari pentru fiecare set de test:')
for i in range(n_e):
    print('Setul',i,': succes in',int(succes[i]),'incercari din',repetari,'(',succes[i]/repetari*100,'%)')
    timp_minim = min(rezultate[i, :, 2])
    timp_maxim = max(rezultate[i, :, 2])
    timp_mediu = np.mean(rezultate[i, :, 2])
    print('Timp: minim -', timp_minim, 'mediu -', timp_mediu, 'maxim - ', timp_maxim)


#Exemplu de rezultate obtinute pentru valorile:
# d_p=100     #dimensiune populatie
# p_r=0.8     #probabilitate recombinare
# p_m=0.1     #probabilitate mutatie
# n_i=250     #numar iteratii
# Rezultate dupa 10 incercari pentru fiecare set de test:
# Setul 0 : succes in 10.0 incercari din 10 ( 100.0 %)
# Timp: minim - 2.260467 mediu - 3.8570179 maxim -  7.17339
# Setul 1 : succes in 10.0 incercari din 10 ( 100.0 %)
# Timp: minim - 2.934431 mediu - 4.1598333 maxim -  7.087158
# Setul 2 : succes in 9.0 incercari din 10 ( 90.0 %)
# Timp: minim - 4.193506 mediu - 7.749890599999999 maxim -  10.393103