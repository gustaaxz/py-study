def cadastro(nome, matricula, setor, cargo):
    dados = [nome, matricula, setor, cargo]
    return dados

nome = input("Qual o seu nome?: ")
matricula = input("Qual a sua matrícula?: ")
setor = input("Qual o seu setor?: ")
cargo = input("Qual o seu cargo?: ")

colaborador = cadastro(nome, matricula, setor, cargo)

print("\n--- Dados do Colaborador ---")
print("Nome:", colaborador[0])
print("Matrícula:", colaborador[1])
print("Setor:", colaborador[2])
print("Cargo:", colaborador[3])

# def cadastro(nome, matricula, setor, cargo): // Cria uma função chamada cadastro, onde é chamada logo abaixo
#   dados = [nome, matricula, setor, cargo]
#   return dados
# 
# nome = input("Qual o seu nome?: ")
# matricula = input("Qual a sua matrícula?: ") 
# setor = input("Qual o seu setor?: ")
# cargo = input("Qual o seu cargo?: ")
#
# colaborador = cadastro(nome, matricula, setor, cargo) // Chama a função cadastro
#
# print("--- Dados do Colaborador ---")
# print("Nome:", colaborador[0]) // Printa o nome no Index 0
# print("Matrícula:", colaborador[1]) // Printa a matrícula no Index 1
# print("Setor:", colaborador[2]) // Printa o setor no Index 2 
# print("Cargo:", colaborador[3]) // Printa o cargo no Index 3