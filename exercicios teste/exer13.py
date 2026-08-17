## Crie uma função que receba como parâmetro uma lista, com valores de qualquer tipo. A função deve imprimir todos os elementos da lista numerando-os

def mostrar_lista(lista) : 
    for numero, elemento in enumerate(lista, start=1) :
        print(numero, "-", elemento)

lista = ["João", 10, 3.5, True, "Python"]
mostrar_lista(lista)