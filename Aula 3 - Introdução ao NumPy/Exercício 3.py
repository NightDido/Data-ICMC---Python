#Crie um array com elementos de 0 a 100 e calcule a soma de todos os valores pares.

import numpy as np

arr = np.arange(101) #crie um array de 0 a 100.
pares_bool = (arr % 2 == 0) #retorna uma matriz de "True" e "False", onde "True" quer dizer que o número é par.
print(arr[pares_bool].sum())#"arr[pares_bool]" troca onde é "True" pelo seus correspondentes da lista original e o ".sum()" soma todos os elementos do array.
#resultado: 2550
