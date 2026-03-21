#Crie um array com elementos de 0 a 100 e calcule a soma de todos os valores pares.

import numpy as np

arr = np.arange(101)
pares_bool = (arr % 2 == 0)
print(arr[pares_bool].sum())
