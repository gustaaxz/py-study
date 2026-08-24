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
