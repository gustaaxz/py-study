horas = float(input("Digite as horas de funcionamento da máquina: "))

if horas <= 500:
    status = "Operação normal"
elif horas <= 1000:
    status = "Programar manutenção"
else:
    status = "Manutenção necessária"

print(f"Status da máquina: {status}")

"""
horas = float(input("Digite as horas de funcionamento da máquina: "))

if horas <= 500:
    status = "Operação normal"
elif horas <= 1000:
    status = "Programar manutenção"
else:
    status = "Manutenção necessária"

print(f"Status da máquina: {status}")
"""