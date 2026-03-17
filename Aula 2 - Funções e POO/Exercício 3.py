#Crie uma função que dado dois vetores, 
#retorne um novo vetor que é a concatenação de ambos os vetores

def Concatenar (vetor1, vetor2):
    NovoVetor = vetor1.copy()

    for elemento in vetor2:
        NovoVetor.append(elemento)
    
    return NovoVetor

vetor1 = [1,2,3]
vetor2 = [4,5,6]

NovoVetor = Concatenar(vetor1, vetor2)

print(NovoVetor)
print(vetor1)