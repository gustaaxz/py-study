materiais = ["Parafuso", "Cabo", "Rolamento", "Terminal"]
quantidades = [5, 30, 8, 50]

print("--- Materiais com estoque abaixo de 10 unidades ---")
for i in range(len(materiais)):
    if quantidades[i] < 10:
        print(f"- {materiais[i]}: {quantidades[i]} unidades")

"""
materiais = ["Parafuso", "Cabo", "Rolamento", "Terminal"] // Cria uma matriz para definir os materiais
quantidades = [5, 30, 8, 50] // Cria uma matriz para definir a quantidade de materiais
--- Ficaria por exemplo: (Parafuso - 5, Cabo - 30, Rolamento - 8, Terminal - 50)

print("--- Materiais com estoque abaixo de 10 unidades ---")
for i in range(len(materiais)): // Cria um for para verificar a quantidade de itens com menos de 10 unidades
    if quantidades[i] < 10: // Faz a verificação
        print(f"- {materiais[i]: {quantidades[i]} unidades}) 
"""