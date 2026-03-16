# Exercício: Desenvolva um programa que selecione um número aleatório entre 0 e 100. O usuário deverá tentar adivinhar esse número. 
# Ao final, o programa exibirá a sequência de palpites do usuário e o total de tentativas feitas até acertar o número correto.

import random

NumeroGerado: int = random.randint(0,100) #NúmeroGerado recebe o valor aleatório entre 0 e 100.
Palpites = [] #Lista para salvar os palpites do usuário.

print(" --- Advinhe o número aleatório entre 0 e 100 ---") #título do jogo.

while (True):
    NumeroUsuario = int(input("Digite um número: ")) #pegando o número.
    Palpites.append(NumeroUsuario) #salvando o número na lista.

    if (NumeroUsuario == NumeroGerado):
        print("Parabéns, você acertou!")
        break #Já que o meu while não para "sozinho", preciso utilizar um break quando o jogador acertar o número sorteado.
    
    elif (NumeroUsuario > NumeroGerado):
        print("Seu número é maior que o sorteado")
    
    else:
        print("O número que você digitou é menor que o sorteado")
    
print("\n -- Resumo da Partida ---")

print("Sua sequência de palpites:", *Palpites, sep=", ") #Utilizando o * para retirar todos os objetos da lista e o comando "sep= " para trocar o delimitador entre eles, normalmente seria só o espaço.
print(f"Quantidade de palpites: {len(Palpites)}")
