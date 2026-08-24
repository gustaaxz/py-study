producao_dias = []

for dia in range(1, 6):
    qtd = int(input(f"Digite a produção do dia {dia}: "))
    producao_dias.append(qtd)

total_produzido = sum(producao_dias)
media_diaria = total_produzido / len(producao_dias)
maior_producao = max(producao_dias)
dia_maior = producao_dias.index(maior_producao) + 1

print("\n--- Relatório de Produção (5 dias) ---")
print(f"Total produzido: {total_produzido} peças")
print(f"Média diária: {media_diaria:.2f} peças/dia")
print(f"Maior produção: {maior_producao} peças (Dia {dia_maior})")

"""
producao_dias = [] // Cria uma matriz onde armazena os dias de produção

for dia in range(1, 6): // Os dias começam no dia 1, e vão até o 5
    qtd = int(input(f"Digite a produção do dia {dia}: ")) // Quantidade de produtos que foram produzidos no dia
    producao_dias.append(qtd) // Adiciona ao final da lista usando .append

total_produzido = sum(producao_dias) // Soma o total de produção de todos os dias
media_diaria = total_produzido / len(producao_dias) // Pega a média diária do dia, dividindo o total pela produção dos dias
maior_producao = max(producao_dias) // Pega a maior produção de todos os dias
dia_maior = producao_dias.index(maior_producao) + 1 // .index procura a posição numérica numa lista

print("--- Relatório de Produção (5 dias) ---")
print(f"Total produzido: {total_produzido} peças")
print(f"Média diária: {media_diaria:.2f} peças/dia")
print(f"Maior produção: {maior_producao} peças (Dia {dia_maior})")
"""