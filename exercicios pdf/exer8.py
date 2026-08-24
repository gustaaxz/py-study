def relatorio_producao(producao):
    total = sum(producao)
    media = total / len(producao)
    maior = max(producao)
    menor = min(producao)
    return total, media, maior, menor

producao = [850, 920, 880, 1050, 990]

total, media, maior, menor = relatorio_producao(producao)

print("--- Relatório de Produção ---")
print(f"Total produzido: {total}")
print(f"Média de produção: {media:.2f}")
print(f"Maior produção: {maior}")
print(f"Menor produção: {menor}")
