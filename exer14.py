## Crie uma função que receba como parâmetro uma lista com valores numéricos e retorne a média desses valores

def calcular_media(lista) :
        media = sum(lista) / len(lista)
        return media
notas = [7, 8, 9, 6]

resultado = calcular_media(notas)
print("Média:", resultado)