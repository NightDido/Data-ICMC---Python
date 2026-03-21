#Faça uma função que receba um array como entrada, remova o primeiro e o último elementos do array
#retorne um novo array contendo os elementos restantes.

import numpy as np

original = np.array([2, 5, 7, 9, 1, 4, 5]) #definimos uma matriz original
def remove_primeiro_último(arr): #como o exercício manda criamos uma função, precisamos usar o "def"
    return arr[1:-1] #retorna o array sem o primeiro elemento (indíce 0), então começa no segundo e vai até o último elemento sem ele estar incluso, podemos usar o "-1" sempre que quiseremos chamar o último elemento.

print(remove_primeiro_último(original)) #retorna [5 7 9 1 4]
