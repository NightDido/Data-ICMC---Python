#Crie uma funçãoq ue dado dois vetores retorne um novo vetor 
#que é composto dos maiores elementos de cada vetor

def vetor_combinado (vetor1, vetor2):
    novo_vetor = []

    novo_vetor.append(max(vetor1)) #Poderiamos utilizar a função do Exercício 1, porém, como existe "max".
    novo_vetor.append(max(vetor2))

    return novo_vetor

vetor1 = [1,2,3]
vetor2 = [30,1,2]

NovoVetor = vetor_combinado(vetor1,vetor2)

print(NovoVetor) #Retornará [3, 30]
