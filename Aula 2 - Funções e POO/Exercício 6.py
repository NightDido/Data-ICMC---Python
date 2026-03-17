#Agora crie uma função que dado um texto e um número retorne o número de 
#palavras que tenham um tamanho maior que o do número fornecido.

import string

def Maiorque(texto, número):
    
    limpador = str.maketrans("", "", string.punctuation)
    texto_limpo = texto.translate(limpador)

    contador = 0
    lista = texto_limpo.split()

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
The whole kingdom celebrated on their wedding day.""" #https://shrek.fandom.com/wiki/Storybook

print(Maiorque(texto, 5))