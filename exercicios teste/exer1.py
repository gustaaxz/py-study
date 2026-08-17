## Escreva um programa que receba 2 valores do tipo inteiro x e y, e calcule o valor de z:
## z = (x² + y²)
#       -------    
#      (x - y)²

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

z = (x**2 + y**2) / (x-y)**2
print("O valor de z é: ", z)