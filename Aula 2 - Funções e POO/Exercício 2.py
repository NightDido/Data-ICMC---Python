#Exercício 2: Você está organizando uma lista de alunos por turma em uma escola.
#Cada turma contém vários alunos, e cada aluno édeve conter um nome, idade e id.

#Mesmo exercício da Aula 1, porém, vamos resolver utilizando o conteúdo que aprendemos sobre POO.

class Aluno():
    def __init__(self, nome, idade, id): # O __init__ define o que cada aluno deve ter assim que for criado, nesse caso, o aluno deve ter: nome, idade e um id.
        self.nome = nome
        self.idade = idade
        self.id = id

class Turma(): 
    def __init__(self, nome): #Cada turma nasce com um nome e uma lista de alunos vazia.
        self.nome = nome
        self.alunos = []
        
    def AdicionarAluno(self, aluno): #Adiciona um objeto da classe Aluno à lista da Turma
        self.alunos.append(aluno)

    def RemoverAluno(self, idAluno): #Procura um aluno pelo id e remove da turma. Procuramos pelo id, pois o id é único, pode ser considerado como a matrícula.
        for aluno in self.alunos:
            if aluno.id == idAluno:
                self.alunos.remove(aluno)
    
    def ListarAlunos(self): #Exibe os alunos de uma turma.
        if len(self.alunos) == 0: #Verificação caso a turma não tenha alunos.
            print("Essa turma não contem alunos")

            return None 
        
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Idade: {aluno.idade}, id: {aluno.id}")

#a) Crie duas turmas, cada uma contendo dois alunos.

turmaA = Turma("turma A")
turmaB = Turma("turma B")

aluno1 = Aluno("aluno1", 20, 1)
aluno2 = Aluno("aluno2", 22, 2)

turmaA.AdicionarAluno(aluno1)
turmaA.AdicionarAluno(aluno2)

turmaB.AdicionarAluno(Aluno("aluno3", 21, 3))
turmaB.AdicionarAluno(Aluno("aluno4", 28, 4))

#b) Adicionar um novo aluno: Adicione um novo aluno em uma das turmas.

turmaA.AdicionarAluno(Aluno("aluno5", 30, 5))

#c) Remover um aluno: Remova um aluno de uma das turmas.

turmaA.RemoverAluno(2)

#d) Exibir os alunos de uma turma.

print(f"Alunos na {turmaA.nome}:")
turmaA.ListarAlunos()

print(f"\nAlunos na {turmaB.nome}:")
turmaB.ListarAlunos()
