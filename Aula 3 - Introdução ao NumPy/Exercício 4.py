#Gere um array A contendo todos os números impares entre 0 a 100. 
#A partir de A, crie outro array que contenha a soma cumulativa 
#dos elementos de A que são divisíveis por 3 e 5.


import numpy as np

arr = np.arange(101)
impares_bool = (arr % 2 != 0)
impares = arr[impares_bool]
div_3_5 = (impares % 3 == 0) & (impares % 5 == 0)
print(impares[div_3_5].cumsum())

