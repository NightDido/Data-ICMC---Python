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
    for j in range (altura - (i + 1)):
        print(" ", end="")
    
    for _ in range (i + 1):
        print("#", end="")
    
    print()
