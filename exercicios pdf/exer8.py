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

"""
def relatorio_producao(producao): // Define uma função passando o parâmetro producao
    total = sum(producao) // Define o total produzido
    media = total / len(producao) // Define a média produzida
    maior = max(producao) // Define qual foi a maior produção
    menor = min(producao) // Define qual foi a menor produção
    return total, media, maior, menor // Retorna todos os valores

producao = [850, 920, 880, 1050, 990] // Define os valores baseado nos parâmetros (total, media, maior, menor)

print("--- Relatório de Produção ---")
print(f"Total produzido: {total}")
print(f"Média de produção: {media:.2f}")
print(f"Maior produção: {maior}")
print(f"Menor produção: {menor}")
"""