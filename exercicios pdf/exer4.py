materiais = ["Parafuso", "Cabo", "Rolamento", "Terminal"]
quantidades = [5, 30, 8, 50]

print("--- Materiais com estoque abaixo de 10 unidades ---")
for i in range(len(materiais)):
    if quantidades[i] < 10:
        print(f"- {materiais[i]}: {quantidades[i]} unidades")
