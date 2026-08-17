## 5. Cálculo de eficiência da produção
# Crie uma função que receba:
# - Quantidade planejada.
# - Quantidade produzida.
# Calcule a eficiência em porcentagem.

def calcular_eficiencia(planejada, realizada):
    if planejada <= 0:
        return 0.0
    eficiencia = (realizada / planejada) * 100
    return eficiencia

planejada = int(input("Produção planejada: "))
realizada = int(input("Produção realizada: "))

eficiencia = calcular_eficiencia(planejada, realizada)
print(f"Eficiência: {eficiencia:.1f}%")
