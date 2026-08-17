## Considere um dicionario com 5 nomes de alunos e suas notas. 
## Escreva um programa que calcule a média dessas notas

alunos = {
    "Capitão América" : 2.0,
    "Homem de Ferro" : 5.0,
    "Homem-Aranha" : 9.0,
    "Superhomem" : 1.0,
    "Thor" : 10.0
} 

media = sum(alunos.values()) / 5
print(media)