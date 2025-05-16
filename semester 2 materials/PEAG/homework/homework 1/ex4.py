import random

def permutari():
    dimensiune = int(input("k: "))
    solutie=[]
    for i in range(15):
        lista = []
        permutare = []
        for i in range(dimensiune):
            lista.append(i + 1)
        for i in range(dimensiune):
            rand = random.choice(lista)
            permutare.append(rand)
            lista.remove(rand)
        quality = 0
        for i in range(dimensiune - 1):
            if (permutare[i]-permutare[i + 1]) % 2 == 0:
                quality = quality + 1
        permutare.append(quality)
        solutie.append(permutare)

    print(solutie)
    max_quality = max(elements[-1] for elements in solutie)
    print(max_quality)


permutari()