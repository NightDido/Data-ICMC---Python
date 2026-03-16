#Exercício: Você está organizando uma lista de alunos por turmas em uma escola. Cada turma contém vários alunos, 
# e cada aluno é representado por um dicionário com informações sobre seu nome e idade.

#a) Criar as turmas: Crie duas turmas, cada uma contendo uma lista de dicionários representando os alunos.
#Cada dicionário deve ter chaves "nome" e "idade".
turmas = { #criamos um dicionário "turmas" que contém a "Turma A" e a "Turma B".
    "Turma A": [ #Cada uma das turmas é uma lista que contém os alunos e suas informações no formato de dicionário.
        {"nome": "aluno1", "idade": 20, "id": 1}, #por mais que o exercício não peça um id, podemos considerar esse id como uma matrícula, facilitando achar os alunos.
        {"nome": "aluno2", "idade": 20, "id": 2}
    ],

    "Turma B":[
        {"nome": "aluno3", "idade": 22, "id":3},
        {"nome": "aluno4", "idade": 23, "id":4}
    ]
}

#b) Adicionar um novo aluno: Adicione um novo aluno em uma das turmas.
NovoAluno = {"nome": "aluno5", "idade": 23, "id": 5}

turmas["Turma A"].append(NovoAluno) #por turma ser uma lista com dicionários, podemos usar o .append

#c) Remover um aluno: Remova um aluno de uma das turmas.
id: int = 3 #para não removermos dois alunos com nomes iguais, utilizamos um id único para cada um.

for turma in turmas.keys(): #com esse for passamos pelas turmas A e B
    for aluno in turmas[turma]: #com esse for passamos pelos alunos em cada turma
        if aluno["id"] == id: #utilizamos o if para achar o aluno com mesmo id proposto no início, nesse caso o id 3.
            turmas[turma].remove(aluno) #removemos o aluno com o id 3.

#d) Exibir os alunos de uma turma.
for turma in turmas.keys():
    print(turma) #retorna Turma A e depois Turma B

    for aluno in turmas[turma]: #retorna os alunos dentro de cada turma.
        print(f"Nome: {aluno["nome"]}, Idade: {aluno["idade"]} ")
    
    print() #quebra de linha para cada aluno
