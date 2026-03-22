#Gere um array A contendo todos os números impares entre 0 a 100. 
#A partir de A, crie outro array que contenha a soma cumulativa 
#dos elementos de A que são divisíveis por 3 e 5.


import numpy as np

arr = np.arange(101) #Gera um array de 0 a 100
impares_bool = (arr % 2 != 0) #Filtra apenas os ímpares, criando "True" caso sejam impares e "False" caso contrário.
impares = arr[impares_bool] #Altera os valores "True" para valores do array com o mesmo índice.
div_3_5 = (impares % 3 == 0) & (impares % 5 == 0) #Filtra os valores impares que são divisiveis por 3 e 5, nesse caso criando "True" e caso contrário "False"
print(impares[div_3_5].cumsum()) #"Impares[div_3_5]" gera um array de [15, 45, 75], o "cumsum()" gera um array que faz a soma acumulativa, gerando [15 60 135]

