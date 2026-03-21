#Faça uma função que receba um array como entrada, remova o primeiro e o último elementos do array
#retorne um novo array contendo os elementos restantes.

import numpy as np

original = np.array([2, 5, 7, 9, 1, 4, 5])
def remove_primeiro_último(arr):
    return arr[1:-1]

print(remove_primeiro_último(original))