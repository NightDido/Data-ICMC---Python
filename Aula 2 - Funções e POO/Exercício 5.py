#Crie uma função que receba uma lista de palavras e retorne o 
#número de palavras que tenham um tamanho maior que 5

def Maiorque5 (ListaPalavras):
    contador = 0

    for palavra in ListaPalavras:
        if len(palavra) > 5:
            contador += 1
    
    return contador

Palavras = ["Olá", "Paralelepipedo", "Python", "ICMC", "Data", "DataICMC"]

print(Maiorque5(Palavras)) #Retornará o valor 3.
