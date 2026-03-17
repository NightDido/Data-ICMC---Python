#Exercício 1: Faça uma função que dado um vetor de inteiros retorne o maior inteiro do vertor.

def MaiorValor(vetor): #para aprender a usar "def", fizemos uma função que retorna o maior valor dentro do vetor. 
    if (len(vetor) ==0): #verificar que o vetor não é vazio.
        return None 
    
    maior = vetor[0] #pegamos o primeiro objeto do vetor e armazenamos.

    for i in range (1, len(vetor)): #começamos no índice 1, pois temos o número que está no índice 0 armazenado na variável "maior".
        if vetor[i] > maior:
            maior = vetor[i]
    
    return maior #retorna o maior número do vetor.
                    
        
vetor = [1, 2, 29, 7] #vetor de teste.

print(MaiorValor(vetor)) #retorna 29.

print(max(vetor)) #como existe o "max", não é necessário criar uma função. Também retorna 29.
