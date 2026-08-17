## 9. Controle de colaboradores por setor
# Crie um programa utilizando listas e dicionários para cadastrar colaboradores.
# Cada colaborador deve possuir: Nome, Matrícula, Setor, Cargo
# O programa deve permitir:
# 1. Cadastrar colaborador
# 2. Listar colaboradores
# 3. Pesquisar colaborador pela matrícula
# 4. Mostrar quantos colaboradores existem em cada setor

# Lista global para armazenar os colaboradores
colaboradores = []


# FUNÇÃO 1: Cadastrar Colaborador
def cadastrar_colaborador():
    nome = input("Digite o nome: ")
    matricula = input("Digite a matrícula: ")
    setor = input("Digite o setor: ")
    cargo = input("Digite o cargo: ")
    
    # Criando o dicionário com as informações
    colaborador = {
        "nome": nome,
        "matricula": matricula,
        "setor": setor,
        "cargo": cargo
    }
    
    colaboradores.append(colaborador)
    print("-> Colaborador cadastrado com sucesso!")


# FUNÇÃO 2: Listar Todos os Colaboradores
def listar_colaboradores():
    if len(colaboradores) == 0:
        print("-> Nenhum colaborador cadastrado ainda.")
    else:
        print("\n--- Lista de Colaboradores ---")
        for c in colaboradores:
            print(f"Matrícula: {c['matricula']} | Nome: {c['nome']} | Setor: {c['setor']} | Cargo: {c['cargo']}")


# FUNÇÃO 3: Pesquisar Colaborador por Matrícula
def pesquisar_por_matricula():
    mat_busca = input("Digite a matrícula para pesquisa: ")
    encontrado = False
    
    for c in colaboradores:
        if c["matricula"] == mat_busca:
            print(f"-> Encontrado! Nome: {c['nome']}, Setor: {c['setor']}, Cargo: {c['cargo']}")
            encontrado = True
            break
            
    if not encontrado:
        print("-> Colaborador não encontrado.")


# FUNÇÃO 4: Mostrar Quantidade por Setor
def mostrar_por_setor():
    if len(colaboradores) == 0:
        print("-> Nenhum colaborador cadastrado.")
    else:
        # Dicionário para contar a quantidade de colaboradores em cada setor
        setores = {}
        for c in colaboradores:
            setor = c["setor"]
            if setor in setores:
                setores[setor] = setores[setor] + 1
            else:
                setores[setor] = 1
        
        print("\n--- Colaboradores por Setor ---")
        for setor, qtd in setores.items():
            print(f"Setor {setor}: {qtd} colaborador(es)")


# --- MENU PRINCIPAL ---
while True:
    print("\n=== MENU COLABORADORES ===")
    print("1. Cadastrar colaborador")
    print("2. Listar colaboradores")
    print("3. Pesquisar por matrícula")
    print("4. Mostrar colaboradores por setor")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_colaborador()
    elif opcao == "2":
        listar_colaboradores()
    elif opcao == "3":
        pesquisar_por_matricula()
    elif opcao == "4":
        mostrar_por_setor()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
