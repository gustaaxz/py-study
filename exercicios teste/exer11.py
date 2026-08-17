## Escreva um programa que leia um numero de 1 a 10 e mostre a tabuada desse numero

numero = int(input("Qual número deseja multiplicar pela tabuada?: "))

for i in range(1, 11) :
    print(f"{numero} x {i} = {numero * i}")