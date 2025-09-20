"""
Larisa Carolina Alvarez Gonzalez 763374
19/09/2025
Calcular la hora correspondiente al segundo siguiente
"""

# Entradas
horas = int(input("Hora: "))
minutos = int(input("Minuto: "))
segundos = int(input("Segundo: "))


# Proceso
segundos = int(segundos) + 1
if segundos > 59:
    minutos += 1
    segundos = 0
    if minutos > 59:
        minutos = 0
        horas += 1
        if horas >= 24:
            horas = 0

horaF = horas
minutoF = minutos
segundoF = segundos

# Salidas
print("Hora final: " )
print("Hora: " + str(horaF))
print("Minuto: " + str(minutos))
print("Segundo: " + str(segundos))