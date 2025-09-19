"""
Larisa Carolina Alvarez Gonzalez 763374
Ximena Castro Lopez 743955
Angelica Ibarra Diaz 761017
Marco Fabricio Azpeitia Castellanos 765168

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
        if horas > 24:
            horas = 0

horaF = horas
minutoF = minutos
segundoF = segundos

# Salidas
print("\n")
print("Hora final: " )
print("Hora: " + str(horaF))
print("Minuto: " + str(minutos))
print("Segundo: " + str(segundos))