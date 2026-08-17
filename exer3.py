## Dada a lista L = [5,7,2,9,4,1,3], escreva um programa que imprima as seguintes funções:
## a) tamanho da lista
## b) maior valor da lista
## c) menor valor da lista
## d) soma de todos os elementos da lista
## e) lista em ordem crescente
## f) lsita em ordem decrescente

L = [5,7,2,9,4,1,3]

print("O tamanho da lista é:", len(L))
print("O maior valor da lista é:", max(L))
print("O menor valor da lista é:", min(L))
print("A soma de todos os elementos da lista é:", sum(L))
print("A lista em ordem crescente é:", sorted(L))
print("A lista em forma decrescente é:", sorted(L, reverse=True))