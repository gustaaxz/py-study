## Refazer exercicio 7, identificando o conceito aprovado (media superior a 6), exame (entre 4 e 6), reprovado (media menor que 4)

nota1 = float(input("Qual a primeira nota?: "))
nota2 = float(input("Qual a segunda nota?: "))

nota = (nota1 + nota2) / 2

if (nota > 6) : 
    print("Você foi aprovado!")
elif (nota >= 4) :
    print("Você está de exame!")
else :
    print("Você está reprovado!")
