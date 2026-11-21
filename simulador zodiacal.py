print("--- DETERMINAR SIGNO ZODIACAL ---")

mes = int(input("Ingresa el número de mes (3 al 7): "))
dia = int(input("Ingresa el día del mes: "))

if (mes == 3 and dia >= 21 and dia <= 31) or (mes == 4 and dia >= 1 and dia <= 19):
    print("Tu signo es: Aries")
elif (mes == 4 and dia >= 20 and dia <= 30) or (mes == 5 and dia >= 1 and dia <= 20):
    print("Tu signo es: Tauro")
elif (mes == 5 and dia >= 21 and dia <= 31) or (mes == 6 and dia >= 1 and dia <= 20):
    print("Tu signo es: Géminis")
elif (mes == 6 and dia >= 21 and dia <= 30) or (mes == 7 and dia >= 1 and dia <= 22):
    print("Tu signo es: Cáncer")
else:
    print("Fecha fuera de rango para Aries, Tauro, Géminis o Cáncer.")
