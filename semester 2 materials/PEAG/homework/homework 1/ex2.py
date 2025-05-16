import numpy as np

def generatePop():
    pop_list = []
    for i in range(18):
        my_list = []
        for i in range(5):
            bit = np.random.randint(0,2)
            my_list.append(bit)
        pop_list.append(my_list)

    for values in pop_list:
        quality = 0
        for i in range(4):
            if values[i] != values[i + 1]:
                quality += 1
            values.append(quality)
    return pop_list

print(generatePop())