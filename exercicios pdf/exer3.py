def calcular_percentual_aprovacao(produzidas, aprovadas, reprovadas):
    if produzidas <= 0:
        return 0.0
    percentual = (aprovadas / produzidas) * 100
    return percentual

produzidas = int(input("Peças produzidas: "))
aprovadas = int(input("Peças aprovadas: "))
reprovadas = int(input("Peças reprovadas: "))

percentual = calcular_percentual_aprovacao(produzidas, aprovadas, reprovadas)
print(f"Percentual de aprovação: {percentual:.1f}%")

"""
def calcular_percentual_aprovacao(produzidas, aprovadas, reprovadas): // Cria uma função onde pega o percentual de peças produzidas, aprovadas e reprovadas
    if produzidas <= 0:
        return 0.0
    percentual = (aprovadas / produzidas) * 100
    return percentual

produzidas = int(input("Peças produzidas: ))
aprovadas = int(input("Peças aprovadas: ))
reprovadas = int(input("Peças reprovadas: ))

percentual = calcular_percentual_aprovacao(produzidas, aprovadas, reprovadas) // Chama a função para calcular o percentual de aprovação das peças
print(f"Percentual de aprovação: {percentual:.1f}%") // Print com a formatação adequada
"""