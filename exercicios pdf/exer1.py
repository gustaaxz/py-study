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