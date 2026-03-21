import numpy as np

#Encotre o intervalo inteiro do desvio padrão em torno da média.

arr = np.linspace(0, 20, 21)
bool_idx = (arr > arr.mean() - arr.std()) & (arr < arr.mean() + arr.std())
valores_intervalo = arr[bool_idx]
intervalo = [valores_intervalo.min().item(), valores_intervalo.max().item()]
print(intervalo)