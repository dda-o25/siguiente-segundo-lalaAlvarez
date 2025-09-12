"""
Larisa Carolina Alvarez Gonzalez 763374
Ximena Castro Lopez 743955
Angelica Ibarra Diaz 761017
Marco Fabricio Azpeitia Castellanos 765168

"""

# Entradas
horas = int(input("Ingrese las horas: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))


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

hora_final = " Hora: " + str(horas) + "\n Minutos: " + str(minutos) + "\n Segundos: " + str(segundos)

# Salidas
print("\n")
print("Hora final: " )
print(hora_final)
