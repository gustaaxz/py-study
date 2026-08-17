## 6. Controle de manutenção
# Crie um programa que receba a quantidade de horas de funcionamento da máquina.
# Classifique:
# - Até 500 horas -> Operação normal
# - De 501 a 1.000 horas -> Programar manutenção
# - Acima de 1.000 horas -> Manutenção necessária

horas = float(input("Digite as horas de funcionamento da máquina: "))

if horas <= 500:
    status = "Operação normal"
elif horas <= 1000:
    status = "Programar manutenção"
else:
    status = "Manutenção necessária"

print(f"Status da máquina: {status}")
