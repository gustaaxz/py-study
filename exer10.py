## Escreva um programa que leia 10 notas e informe a média dos alunos

notas = [1,2,3,4,5,6,7,8,9,4]
soma = 0

for nota in notas :
    soma = soma + nota

print(soma / len(notas))