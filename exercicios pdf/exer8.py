## 8. Relatório de produção
# Crie uma função que receba uma lista contendo a produção diária de uma linha do parque fabril.
# A função deve retornar:
# - Total produzido.
# - Média de produção.
# - Maior produção.
# - Menor produção.

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
