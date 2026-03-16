#Exercício: Você está organizando uma lista de alunos por turmas em uma escola. Cada turma contém vários alunos, 
# e cada aluno é representado por um dicionário com informações sobre seu nome e idade.

#a) Criar as turmas: Crie duas turmas, cada uma contendo uma lista de dicionários representando os alunos.
#Cada dicionário deve ter chaves "nome" e "idade";

#b) Adicionar um novo aluno: Adicione um novo aluno em uma das turmas.

#c) Remover um aluno: Remova um aluno de uma das turmas.

#d) Exibir os alunos de uma turma.

#a)
turmas = {
    "Turma A": [
        {"nome": "aluno1", "idade": 20, "id": 1},
        {"nome": "aluno2", "idade": 20, "id": 2}
    ],

    "Turma B":[
        {"nome": "aluno3", "idade": 22, "id":3},
        {"nome": "aluno4", "idade": 23, "id":4}
    ]
}

#b)
NovoAluno = {"nome": "aluno5", "idade": 23, "id": 5}

turmas["Turma A"].append(NovoAluno)

#c)
id: int = 3

for turma in turmas.keys():
    for aluno in turmas[turma]:
        if aluno["id"] == id:
            turmas[turma].remove(aluno)


#d)
for turma in turmas.keys():
    print(turma)

    print("Alunos: ")

    for aluno in turmas[turma]:
        print(f"Nome: {aluno["nome"]}, Idade: {aluno["idade"]} ")
    
    print()