def cadastro(nome, matricula, setor, cargo):
    dados = [nome, matricula, setor, cargo]
    return dados
    
# Lendo os dados do usuário
nome = input("Qual o seu nome?: ")
matricula = input("Qual a sua matrícula?: ")
setor = input("Qual o seu setor?: ")
cargo = input("Qual o seu cargo?: ")

# Chamando a função e salvando o retorno
colaborador = cadastro(nome, matricula, setor, cargo)

# Exibindo os dados
print("\n--- Dados do Colaborador ---")
print("Nome:", colaborador[0])
print("Matrícula:", colaborador[1])
print("Setor:", colaborador[2])
print("Cargo:", colaborador[3])