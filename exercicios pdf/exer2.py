## 2. Controle de produção
# Um colaborador precisa registrar a quantidade de peças produzidas durante 5 dias.
# Crie um programa que:
# - Receba a produção de cada dia.
# - Calcule o total produzido.
# - Calcule a média diária.
# - Mostre o dia de maior produção.

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
