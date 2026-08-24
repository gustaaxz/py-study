colaboradores = []
maquinas = []
producoes = []


def cadastrar_colaborador():
    nome = input("Nome do colaborador: ")
    matricula = input("Matrícula: ")
    colaboradores.append({"nome": nome, "matricula": matricula})
    print("-> Colaborador cadastrado com sucesso!")


def cadastrar_maquina():
    nome_maquina = input("Nome ou código da máquina: ")
    maquinas.append(nome_maquina)
    print("-> Máquina cadastrada com sucesso!")


def registrar_producao():
    if len(maquinas) == 0:
        print("-> Nenhuma máquina cadastrada. Cadastre uma máquina primeiro!")
        return
    
    print("\nMáquinas cadastradas:")
    for m in maquinas:
        print(f"- {m}")
    
    nome_m = input("Digite o nome da máquina que produziu: ")
    qtd = int(input("Quantidade de peças produzidas: "))
    
    producoes.append({
        "maquina": nome_m,
        "produzidas": qtd,
        "aprovadas": 0,
        "reprovadas": 0
    })
    print("-> Produção registrada!")


def registrar_inspecao():
    if len(producoes) == 0:
        print("-> Nenhuma produção registrada ainda.")
        return
    
    print("\nRegistros de produção:")
    pos = 1
    for p in producoes:
        print(f"{pos}. Máquina: {p['maquina']} | Produzidas: {p['produzidas']}")
        pos = pos + 1
    
    indice = int(input("Digite o número do registro para inspecionar: ")) - 1
    
    if indice >= 0 and indice < len(producoes):
        aprovadas = int(input("Quantidade de peças aprovadas: "))
        reprovadas = int(input("Quantidade de peças reprovadas: "))
        
        producoes[indice]["aprovadas"] = aprovadas
        producoes[indice]["reprovadas"] = reprovadas
        print("-> Inspeção registrada!")
    else:
        print("-> Registro inválido!")


def consultar_producao():
    if len(producoes) == 0:
        print("-> Nenhum registro encontrado.")
        return
    
    print("\n--- Consultar Produções ---")
    for p in producoes:
        produzidas = p["produzidas"]
        aprovadas = p["aprovadas"]
        
        if produzidas > 0:
            qualidade = (aprovadas / produzidas) * 100
        else:
            qualidade = 0.0
        
        print(f"Máquina: {p['maquina']} | Produzidas: {produzidas} | Aprovadas: {aprovadas} | Reprovadas: {p['reprovadas']} | Qualidade: {qualidade:.1f}%")


def relatorio_producao():
    if len(producoes) == 0:
        print("-> Sem dados para relatório.")
        return
    
    total_produzido = 0
    total_aprovadas = 0
    total_reprovadas = 0
    
    for p in producoes:
        total_produzido = total_produzido + p["produzidas"]
        total_aprovadas = total_aprovadas + p["aprovadas"]
        total_reprovadas = total_reprovadas + p["reprovadas"]
    
    if total_produzido > 0:
        qualidade_geral = (total_aprovadas / total_produzido) * 100
    else:
        qualidade_geral = 0.0
    
    maior_qtd = -1
    maior_maquina = ""
    for p in producoes:
        if p["produzidas"] > maior_qtd:
            maior_qtd = p["produzidas"]
            maior_maquina = p["maquina"]

    print("\n====================================")
    print(" RELATÓRIO FINAL DO PARQUE FABRIL")
    print("====================================")
    print(f"Total de colaboradores: {len(colaboradores)}")
    print(f"Total de máquinas: {len(maquinas)}")
    print(f"Total de peças produzidas: {total_produzido}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Percentual de qualidade geral: {qualidade_geral:.1f}%")
    print(f"Máquina com maior produção: {maior_maquina} ({maior_qtd} peças)")
    print("====================================")


while True:
    print("\n====================================")
    print(" CONTROLE DO PARQUE FABRIL")
    print("====================================")
    print("1 - Cadastrar colaborador")
    print("2 - Cadastrar máquina")
    print("3 - Registrar produção")
    print("4 - Registrar inspeção de qualidade")
    print("5 - Consultar produção")
    print("6 - Relatório da produção")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_colaborador()
    elif opcao == "2":
        cadastrar_maquina()
    elif opcao == "3":
        registrar_producao()
    elif opcao == "4":
        registrar_inspecao()
    elif opcao == "5":
        consultar_producao()
    elif opcao == "6":
        relatorio_producao()
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida!")

"""
colaboradores = [] // Lista para armazenar os colaboradores
maquinas = [] // Lista para armazenar os nomes ou códigos das máquinas
producoes = [] // Lista para armazenar os registros de produção


def cadastrar_colaborador(): // Cria uma função para cadastrar colaborador
    nome = input("Nome do colaborador: ")
    matricula = input("Matrícula: ")
    colaboradores.append({"nome": nome, "matricula": matricula}) // Adiciona o dicionário do colaborador na lista
    print("-> Colaborador cadastrado com sucesso!")


def cadastrar_maquina(): // Cria uma função para cadastrar máquina
    nome_maquina = input("Nome ou código da máquina: ")
    maquinas.append(nome_maquina) // Adiciona a máquina na lista de máquinas
    print("-> Máquina cadastrada com sucesso!")


def registrar_producao(): // Cria uma função para registrar a produção de uma máquina
    if len(maquinas) == 0: // Verifica se há máquinas cadastradas
        print("-> Nenhuma máquina cadastrada. Cadastre uma máquina primeiro!")
        return
    
    print("\nMáquinas cadastradas:")
    for m in maquinas: // Exibe todas as máquinas disponíveis
        print(f"- {m}")
    
    nome_m = input("Digite o nome da máquina que produziu: ")
    qtd = int(input("Quantidade de peças produzidas: "))
    
    producoes.append({
        "maquina": nome_m,
        "produzidas": qtd,
        "aprovadas": 0,
        "reprovadas": 0
    }) // Adiciona o registro da produção com contadores zerados
    print("-> Produção registrada!")


def registrar_inspecao(): // Cria uma função para registrar a inspeção de qualidade
    if len(producoes) == 0: // Verifica se há produções para inspecionar
        print("-> Nenhuma produção registrada ainda.")
        return
    
    print("\nRegistros de produção:")
    pos = 1
    for p in producoes: // Lista os registros com número sequencial
        print(f"{pos}. Máquina: {p['maquina']} | Produzidas: {p['produzidas']}")
        pos = pos + 1
    
    indice = int(input("Digite o número do registro para inspecionar: ")) - 1 // Converte para índice (base 0)
    
    if indice >= 0 and indice < len(producoes): // Valida se o índice está dentro da lista
        aprovadas = int(input("Quantidade de peças aprovadas: "))
        reprovadas = int(input("Quantidade de peças reprovadas: "))
        
        producoes[indice]["aprovadas"] = aprovadas // Atualiza peças aprovadas
        producoes[indice]["reprovadas"] = reprovadas // Atualiza peças reprovadas
        print("-> Inspeção registrada!")
    else:
        print("-> Registro inválido!")


def consultar_producao(): // Cria uma função para consultar todas as produções e qualidade
    if len(producoes) == 0: // Verifica se existem produções cadastradas
        print("-> Nenhum registro encontrado.")
        return
    
    print("\n--- Consultar Produções ---")
    for p in producoes: // Percorre cada registro de produção
        produzidas = p["produzidas"]
        aprovadas = p["aprovadas"]
        
        if produzidas > 0: // Calcula a taxa percentual de qualidade
            qualidade = (aprovadas / produzidas) * 100
        else:
            qualidade = 0.0
        
        print(f"Máquina: {p['maquina']} | Produzidas: {produzidas} | Aprovadas: {aprovadas} | Reprovadas: {p['reprovadas']} | Qualidade: {qualidade:.1f}%")


def relatorio_producao(): // Cria uma função para gerar o relatório consolidado final
    if len(producoes) == 0: // Verifica se há dados para o relatório
        print("-> Sem dados para relatório.")
        return
    
    total_produzido = 0
    total_aprovadas = 0
    total_reprovadas = 0
    
    for p in producoes: // Soma os totais de peças produzidas, aprovadas e reprovadas
        total_produzido = total_produzido + p["produzidas"]
        total_aprovadas = total_aprovadas + p["aprovadas"]
        total_reprovadas = total_reprovadas + p["reprovadas"]
    
    if total_produzido > 0: // Calcula o percentual de qualidade geral
        qualidade_geral = (total_aprovadas / total_produzido) * 100
    else:
        qualidade_geral = 0.0
    
    maior_qtd = -1
    maior_maquina = ""
    for p in producoes: // Descobre a máquina com o maior volume de produção
        if p["produzidas"] > maior_qtd:
            maior_qtd = p["produzidas"]
            maior_maquina = p["maquina"]

    print("\n====================================")
    print(" RELATÓRIO FINAL DO PARQUE FABRIL")
    print("====================================")
    print(f"Total de colaboradores: {len(colaboradores)}")
    print(f"Total de máquinas: {len(maquinas)}")
    print(f"Total de peças produzidas: {total_produzido}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Percentual de qualidade geral: {qualidade_geral:.1f}%")
    print(f"Máquina com maior produção: {maior_maquina} ({maior_qtd} peças)")
    print("====================================")


while True: // Loop principal do menu
    print("\n====================================")
    print(" CONTROLE DO PARQUE FABRIL")
    print("====================================")
    print("1 - Cadastrar colaborador")
    print("2 - Cadastrar máquina")
    print("3 - Registrar produção")
    print("4 - Registrar inspeção de qualidade")
    print("5 - Consultar produção")
    print("6 - Relatório da produção")
    print("0 - Sair")
    
    opcao = input("Escolha uma opção: ") // Recebe a opção do usuário

    if opcao == "1": // Chama cadastro de colaborador
        cadastrar_colaborador()
    elif opcao == "2": // Chama cadastro de máquina
        cadastrar_maquina()
    elif opcao == "3": // Chama registro de produção
        registrar_producao()
    elif opcao == "4": // Chama registro de inspeção
        registrar_inspecao()
    elif opcao == "5": // Chama consulta de produção
        consultar_producao()
    elif opcao == "6": // Chama relatório consolidado
        relatorio_producao()
    elif opcao == "0": // Encerra o programa
        print("Encerrando o sistema...")
        break
    else: // Opção inválida
        print("Opção inválida!")
"""
