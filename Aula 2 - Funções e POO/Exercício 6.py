#Agora crie uma função que dado um texto e um número retorne o número de 
#palavras que tenham um tamanho maior que o do número fornecido.

import string

def Maiorque(texto, número):
    
    limpador = str.maketrans("", "", string.punctuation) #Limpador de pontuação como , e . contidos no texto
    texto_limpo = texto.translate(limpador)#Armazenamos o texto limpo em uma variável.

    contador = 0
    lista = texto_limpo.split() #Utilizamos o .split para criar uma lista com cada palavra do texto. O () vazio, significa que excluirá os espaços e \n contidos no texto.

    for palavra in lista:
        if len(palavra) > número:
            contador += 1
    
    return contador

texto = """Once upon a time, there was a lovely princess. 
But she had an enchantment upon her of a fearful sort. 
Which would only be broken by love's first kiss. 
She was locked away in a castle, guarded by a terrible fire breathing dragon. 
Many brave knights attempted to free her from this dreadful prison, but none prevailed. 
She waited in the Dragon's Keep, in the highest room of the tallest tower. 
For her true love and true love's first kiss. And so it came to pass that a brave knight came to her rescue,
and with a kiss broke the powerful enchantment. 
The whole kingdom celebrated on their wedding day.""" #texto: https://shrek.fandom.com/wiki/Storybook

print(Maiorque(texto, 5)) #Retornará o valor 27.
