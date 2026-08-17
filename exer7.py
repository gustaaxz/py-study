## Faça um programa que leia 2 notas de um aluno, calcule a média e impriva aprovado ou reprovado (media 6)

nota1 = float(input("Qual a primeira nota?: "))
nota2 = float(input("Qual a segunda nota?: "))

nota = nota1 + nota2 / 2

if(nota >= 6) : 
    print("Você passou!")
else : 
    print("Você reprovou!")
