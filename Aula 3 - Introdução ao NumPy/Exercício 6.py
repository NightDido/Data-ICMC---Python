#Considere um array bidimensional no qual cada vetor de uma dimensão possui 3 pontuações
#que um jogador recebeu em 3 provas distintas. Faça uma função que dado esse array,
#retorne a prova com a maior soma de pontuação.

import numpy as np

pontuações = [[6.5, 7.8, 5.4], [9.5, 8.8, 9.1], [4.5, 7.3, 5.9]]

arr = np.array(pontuações)
arr_soma = np.sum(arr, axis=0)
print(arr_soma.max())