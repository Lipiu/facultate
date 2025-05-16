#Construire fisier de test pe baza unui mesaj citit de la tastatura

import numpy

print('\nAtentie! Mesajul pentru codificare trebuie sa contina EXCLUSIV litere mici (a-z), fara spatii!')
m=input('Mesaj pentru codificare:')

print('Mesaj original primit:',m)

cheie=numpy.random.permutation(26)                                      #cheia cu care se face codificarea

n=len(m)
alfa=[chr(int(i + ord('a'))) for i in range(26)]                        #lista cu alfabetul
codificat=[ alfa[int(cheie[ord(m[i])-ord('a')])] for i in range(n)]     #lista cu literele codificate

m_cod=''.join(codificat)                                                #mesaj codificat
print('Mesaj codificat:',m_cod)

print('Numele fisierului de test care va fi creat in directorul curent: nume.extensie')
fo=input('Nume fisier:')
f = open(fo, "w")
f.write(m+'\n')
f.write(m_cod+'\n')
f.close()

fc=fo.split('.')[0]+'-cheie.'+fo.split('.')[1]
f=open(fc,'w')
f.write('['+' '.join(str(lit) for lit in cheie)+']\n')
f.close()
