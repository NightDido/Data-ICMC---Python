#Crie uma função que dado dois vetores, 
#retorne um novo vetor que é a concatenação de ambos os vetores

def Concatenar (vetor1, vetor2): #Une um vetor no outro.
    NovoVetor = vetor1.copy() #Se não usarmos o .copy, a função afetará o vetor1.

    for elemento in vetor2: 
        NovoVetor.append(elemento)
    
    return NovoVetor

vetor1 = [1,2,3]
vetor2 = [4,5,6]

NovoVetor = Concatenar(vetor1, vetor2)

print(NovoVetor) #Retornará [1,2,3,4,5,6].
print(vetor1) #Retornará [1,2,3], pois usamos copy anteriormente.
