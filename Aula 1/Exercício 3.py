#Recrie a pirâmide do Mario.
#O tamanho da pirâmide será decidida pelo usuário, por exemplo: uma pirâmide de tamanho 5 será: 

#       #
#      ##
#     ###
#    ####
#   #####

altura = int(input("Digite a altura da pirâmide: "))

while (altura <=0):
    print("A altura da pirâmide deve ser maior do que zero")
    altura = int(input("Digite um valor diferente para a altura: "))

for i in range(altura):
    for j in range (altura - (i + 1)): #número de espaços necessários até a #
        print(" ", end="")
    
    for _ in range (i + 1): #número de hastags para formar a pirâmide
        print("#", end="")
    
    print() #como temos o end="", precisamos dar um espaço para cada linha

#forma mais eficiente:

for i in range(altura):
    print(" " * (altura - (i + 1)) + "#" * (i + 1)) #fazemos um print de espaços baseados na altura escohlida pelo usuário -1, depois adicionamos uma hashtag. No próximo i, temos espaçoes até a altura -2 e 2 hashtags.
    
