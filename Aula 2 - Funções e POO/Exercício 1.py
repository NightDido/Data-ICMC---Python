#Exercício 1: Faça uma função que dado um vetor de inteiros retorne o maior inteiro do vertor.

def MaiorValor(vetor):
    if (len(vetor) ==0):
        return None
    
    maior = vetor[0]

    for i in range (1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    
    return maior
                    
        
vetor = [1, 2, 29, 7]

print(MaiorValor(vetor))

print(max(vetor))