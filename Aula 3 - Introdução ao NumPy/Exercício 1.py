#Encotre o intervalo inteiro do desvio padrão em torno da média.

import numpy as np

arr = np.linspace(0, 20, 21) #cria uma matriz do 0 a 20, contendo 21 números, com espaçamento de 1 em 1. Caso quisessemos que a matriz tenha 11 números, eles seriam espaçados em 2 em 2.

#criaremos uma matriz de valores booleanos, os que retornam o valor "True" precisam estar no intervalo inteiro do desvio padrão.
bool_idx = (arr > arr.mean() - arr.std()) & (arr < arr.mean() + arr.std()) #o "arr.mean" é a média do meu intervalo original, nesse caso 10.0, e o "arr.std" é o meu desvio padrão, nesse caso, aproximadamente, 6.0553.

valores_intervalo = arr[bool_idx] #pegamos os valores que retornaram "True" e trocamos pelos seus correspondentes da lista original, gerando uma lista que começa em 4 e termina em 16.

#como queremos apenas o intervalo e não a lista completa, pegamos o mínimo e o máximo da lista.
intervalo = [valores_intervalo.min().item(), valores_intervalo.max().item()] #o "item()" converte os elementos do NumPy de volta para os tipos nativos do Python. Caso contrário, teriamos "[np.float64(4.0), np.float64(16.0)]".

print(intervalo) #[4.0, 16.0]
