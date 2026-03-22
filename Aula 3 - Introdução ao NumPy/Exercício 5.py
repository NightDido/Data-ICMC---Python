#Faça uma função que dado dois vetores (valores e pesos), calcule a média ponderada de valores dos seus respectivos pesos.
#Obs: não é permitido utilizar a função np.avarage do NumPy

import numpy as np
valores = np.array ([1, 2, 5])
pesos = np.array ([3, 2, 1])

def media_ponderada (valores, pesos):
    return np.sum(valores * pesos) / np.sum(pesos) #(valores * pesos) gera um array [3 4 5], o "np.sum()" soma esse array retornando um número. A mesma coisa acontece com o array "pesos"

print(media_ponderada(valores,pesos)) #retorna o valor 2.0
